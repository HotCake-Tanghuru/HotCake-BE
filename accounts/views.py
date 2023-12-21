import environ
from pathlib import Path
import requests

from django.contrib.auth import get_user_model
from django.shortcuts import redirect, get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, Follow
from .serializers import UserSerializer, LogoutSerializer, UserProfileSerializer, FollowSerializer
from .permissions import IsOwnerOrReadOnly


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(env_file=BASE_DIR / ".env")

kakao_login_uri = "https://kauth.kakao.com/oauth/authorize"
kakao_token_uri = "https://kauth.kakao.com/oauth/token"
kakao_user_uri = "https://kapi.kakao.com/v2/user/me"
kakao_logout_uri = "https://kauth.kakao.com/oauth/logout"
kakao_unlink_uri = "https://kapi.kakao.com/v1/user/unlink"


class KakaoLogin(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        """카카오 인가 코드를 받기 위한 url을 만들어서 리다이렉트"""
        client_id = env("KAKAO_REST_API_KEY")
        redirect_uri = env("KAKAO_REDIRECT_URI")
        uri = f"{kakao_login_uri}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        res = redirect(uri)
        return res


class KakaoCallback(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def get(self, request):
        """access_token과 회원정보를 요청"""
        # access_token 요청
        code = request.GET.get("code")
        if not code:
            return Response(
                {"message": "code가 없습니다."}, status=status.HTTP_400_BAD_REQUEST
            )

        request_data = {
            "grant_type": "authorization_code",
            "client_id": env("KAKAO_REST_API_KEY"),
            "redirect_uri": env("KAKAO_REDIRECT_URI"),
            "client_secret": env("KAKAO_CLIENT_SECRET_KEY"),
            "code": code,
        }
        token_headers = {
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
        }
        token_res = requests.post(
            kakao_token_uri, data=request_data, headers=token_headers
        )

        token_json = token_res.json()
        kakao_access_token = token_json.get("access_token")

        if not kakao_access_token:
            return Response(
                {"message": "access_token이 없습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        request.session["kakao_access_token"] = kakao_access_token

        kakao_access_token = f"Bearer {kakao_access_token}"

        # 카카오 회원정보 요청
        auth_headers = {
            "Authorization": kakao_access_token,
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        user_info_res = requests.post(kakao_user_uri, headers=auth_headers)
        user_info_json = user_info_res.json()

        social_type = "kakao"
        social_id = f"{social_type}_{user_info_json.get('id')}"

        kakao_account = user_info_json.get("kakao_account")

        if not kakao_account:
            return Response(
                {"message": "카카오 계정이 없습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user_email = kakao_account.get("email")
        profile = kakao_account.get("profile")

        user_nickname = profile.get("nickname")
        user_profile_img = profile.get("profile_image_url")

        user, created = User.objects.get_or_create(
            social_id=social_id,
            defaults={
                "social_type": social_type,
                "social_id": social_id,
                "email": user_email,
                "nickname": user_nickname,
                "profile_img": user_profile_img,
            },
        )

        # 생성된 경우와 기존 사용자인 경우에 따라 다른 메시지 반환
        if created:
            message = "사용자 생성 완료"
        else:
            message = "로그인 완료"

        # JWT 토큰 생성
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        res = {
            "message": message,
            "user": UserSerializer(user).data,
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

        response = Response(res, status=status.HTTP_200_OK)
        return response


class KakaoLogout(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        """카카오계정과 함께 로그아웃"""
        client_id = env("KAKAO_REST_API_KEY")
        logout_redirect_uri = env("KAKAO_LOGOUT_REDIRECT_URI")
        uri = f"{kakao_logout_uri}?client_id={client_id}&logout_redirect_uri={logout_redirect_uri}"
        res = redirect(uri)
        return res


class KakaoLogoutCallback(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    def post(self, request):
        """JWT 토큰을 블랙리스트에 추가"""
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)


class KakaoUnlink(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        """카카오계정과 함께 회원탈퇴"""
        kakao_access_token = request.session.get("kakao_access_token")
        if not kakao_access_token:
            return Response(
                {"message": "access_token이 없습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        kakao_access_token = f"Bearer {kakao_access_token}"

        # 카카오 연결끊기 요청
        auth_headers = {
            "Authorization": kakao_access_token,
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        unlinked_res = requests.post(kakao_unlink_uri, headers=auth_headers)
        unlinked_json = unlinked_res.json()

        social_type = "kakao"
        social_id = f"{social_type}_{unlinked_json.get('id')}"

        user = User.objects.get(social_id=social_id)
        user.delete()

        return Response(status=status.HTTP_200_OK)



class FollowingView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowSerializer
    """팔로잉 목록 조회"""

    def get(self, request, user_id):
        # 사용자 확인
        if not User.objects.filter(id=user_id).exists():
            return Response(
                {"message": "사용자가 존재하지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = User.objects.get(id=user_id)
        # 팔로잉 목록 조회
        following_list = Follow.objects.filter(from_user=user)
        # 팔로잉 목록과 사용자의 정보를 반환
        serializer = self.serializer_class(following_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """팔로잉 추가"""

    def patch(self, request, user_id):
        # 사용자 확인
        if not User.objects.filter(id=user_id).exists():
            return Response(
                {"message": "사용자가 존재하지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = User.objects.get(id=user_id)

        # 팔로잉 대상 확인
        following_user_id = request.data.get("following_user_id")
        if not User.objects.filter(id=following_user_id).exists():
            return Response(
                {"message": "팔로잉 대상이 존재하지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # 팔로잉 대상이 본인인 경우
        if user_id == following_user_id:
            return Response(
                {"message": "본인을 팔로잉 할 수 없습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        following_user = User.objects.get(id=following_user_id)

        # 이미 팔로잉 중이라면, 팔로잉 취소
        if Follow.objects.filter(from_user=user, to_user=following_user).exists():
            Follow.objects.filter(from_user=user, to_user=following_user).delete()
            return Response(
                {"message": "팔로잉 취소 완료"},
                status=status.HTTP_200_OK,
            )

        # 팔로잉 추가
        following = Follow.objects.create(from_user=user, to_user=following_user)
        serializer = self.serializer_class(following)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

class FollowerView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowSerializer
    """팔로워 목록 조회"""

    def get(self, request, user_id):
        # 사용자 확인
        if not User.objects.filter(id=user_id).exists():
            return Response(
                {"message": "사용자가 존재하지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = User.objects.get(id=user_id)
        # 팔로워 목록 조회
        follower_list = Follow.objects.filter(to_user=user)
        # 팔로워 목록과 사용자의 정보를 반환
        serializer = self.serializer_class(follower_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    """팔로워 삭제"""

    def delete(self, request, user_id):
        # 팔로워 확인
        follower_id = request.data.get("follower_user_id")
        if not User.objects.filter(id=follower_id).exists():
            return Response(
                {"message": "팔로워가 존재하지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        follower = User.objects.get(id=follower_id)
        # 팔로워 데이터 확인
        if not Follow.objects.filter(from_user=follower, to_user=user_id).exists():
            return Response(
                {"message": "팔로워 데이터가 존재하지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # 팔로워 삭제
        Follow.objects.filter(from_user=follower, to_user=user_id).delete()
        return Response(
            {"message": "팔로워 삭제 완료"},
            status=status.HTTP_200_OK,
        )

class UserProfileView(GenericAPIView):
    # 인증된 사용자만 접근 가능하고, 소유자만 수정 가능하도록 설정
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = UserProfileSerializer

    def get_object(self):
        """URL에서 pk를 가져와 해당하는 User 인스턴스 반환"""
        pk = self.kwargs.get("pk")
        return get_object_or_404(get_user_model(), pk=pk)

    def get(self, request, *args, **kwargs):
        """프로필 조회"""
        instance = self.get_object()
        self.check_object_permissions(request, instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        """프로필 수정"""
        instance = self.get_object()
        self.check_object_permissions(self.request, instance)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

