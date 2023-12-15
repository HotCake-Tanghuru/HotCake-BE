import environ
from pathlib import Path
import requests


from django.shortcuts import redirect
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(env_file=BASE_DIR / ".env")

kakao_login_uri = "https://kauth.kakao.com/oauth/authorize"
kakao_token_uri = "https://kauth.kakao.com/oauth/token"
kakao_profile_uri = "https://kapi.kakao.com/v2/user/me"


class KakaoLogin(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        """카카오 인가 코드를 받기 위한 url을 만들어서 리다이렉트"""
        client_id = env("KAKAO_REST_API_KEY")
        redirect_uri = env("KAKAO_REDIRECT_URI")
        uri = f"{kakao_login_uri}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        print(uri)
        res = redirect(uri)
        return res


class KakaoCallback(APIView):
    permission_classes = [AllowAny]

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
        access_token = token_json.get("access_token")

        if not access_token:
            return Response(
                {"message": "access_token이 없습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        access_token = f"Bearer {access_token}"

        # 카카오 회원정보 요청
        auth_headers = {
            "Authorization": access_token,
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        user_info_res = requests.post(kakao_profile_uri, headers=auth_headers)
        user_info_json = user_info_res.json()
        # print("=====user_info_json=====")
        # print(user_info_json)

        social_type = "kakao"
        social_id = user_info_json.get("id")

        kakao_account = user_info_json.get("kakao_account")
        # print("=====kakao_account=====")
        # print(kakao_account)

        if not kakao_account:
            return Response(
                {"message": "카카오 계정이 없습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user_email = kakao_account.get("email")
        profile = kakao_account.get("profile")
        # print("=====user_profile=====")
        # print(profile)

        if not profile:
            return Response(
                {"message": "카카오 프로필이 없습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user_nickname = profile.get("nickname")
        user_profile_img = profile.get("profile_image_url")

        res = {
            "social_type": social_type,
            "social_id": social_id,
            "user_email": user_email,
            "user_nickname": user_nickname,
            "user_profile_img": user_profile_img,
        }
        # print("=====res=====")
        # print(res)

        response = Response(res, status=status.HTTP_200_OK)
        response.data = res
        return response
