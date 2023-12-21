from django.test import TestCase, Client, RequestFactory
from unittest.mock import patch, MagicMock
from rest_framework import status
from rest_framework.test import APIClient
from accounts.views import KakaoCallback
from accounts.models import User, Follow
from rest_framework.test import APIClient


class KakaoLoginTest(TestCase):
    """KakaoLogin 뷰에 대한 테스트 케이스"""

    def setUp(self):
        """테스트 케이스의 공통 설정 처리"""
        self.client = Client()

    def test_kakao_login_redirects(self):
        """KakaoLogin 뷰가 정상적으로 리다이렉트하는지 테스트"""
        header = {"HTTP_Authorization": "access_token"}
        response = self.client.get(
            "/oauth/kakao/login/", content_type="application/json", **header
        )
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)


class KakaoCallbackTest(TestCase):
    """KakaoCallback 뷰에 대한 테스트 케이스"""

    # views.py에서
    # request.session["kakao_access_token"] = kakao_access_token 부분을 지우고 테스트 수행!
    # 테스트 수행 후 다시 복구할 것!
    def setUp(self):
        """테스트 케이스의 공통 설정 처리"""
        self.factory = RequestFactory()
        self.view = KakaoCallback.as_view()

    @patch("requests.post")
    @patch("rest_framework_simplejwt.tokens.RefreshToken.for_user")
    def test_kakao_callback(self, mock_for_user, mocked_post):
        """KakaoCallback 뷰가 정상적으로 회원 정보를 반환하는지 테스트"""

        # RefreshToken.for_user 메서드를 가짜로 대체하고, 가짜 토큰 생성
        mock_token = MagicMock()
        mock_token.access_token = "fake_access_token"
        mock_token.__str__.return_value = "fake_refresh_token"
        mock_for_user.return_value = mock_token

        # requests.post 메서드를 가짜로 대체하고, 가짜 응답 생성
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "access_token": "fake_access_token",
            "id": "12345",
            "kakao_account": {
                "email": "user@email.com",
                "profile": {
                    "nickname": "nickname",
                    "profile_image_url": "image_url",
                },
            },
        }
        mocked_post.return_value = mock_response

        # 테스트 요청 생성 후, 뷰 호출
        request = self.factory.get("/oauth/kakao/callback", {"code": "fake_code"})
        response = self.view(request)

        # 예상 응답 설정
        expected_response = {
            "message": "사용자 생성 완료",
            "user": {
                "social_id": "kakao_12345",
                "social_type": "kakao",
                "email": "user@email.com",
                "nickname": "nickname",
                "profile_img": "/image_url",
                "bio": None,
            },
            "access_token": "fake_access_token",
            "refresh_token": "fake_refresh_token",
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, expected_response)

    @patch("requests.post")
    @patch("rest_framework_simplejwt.tokens.RefreshToken.for_user")
    def test_kakao_callback_login(self, mock_for_user, mocked_post):
        """KakaoCallback 뷰가 정상적으로 로그인을 처리하는지 테스트"""

        # 먼저 사용자 생성
        User.objects.create(
            social_type="kakao",
            social_id="kakao_12345",
            email="user@email.com",
            nickname="nickname",
            profile_img="image_url",
        )

        # RefreshToken.for_user 메서드를 가짜로 대체하고, 가짜 토큰 생성
        mock_token = MagicMock()
        mock_token.access_token = "fake_access_token"
        mock_token.__str__.return_value = "fake_refresh_token"
        mock_for_user.return_value = mock_token

        # requests.post 메서드를 가짜로 대체하고, 가짜 응답 생성
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "access_token": "fake_access_token",
            "id": "12345",
            "kakao_account": {
                "email": "user@email.com",
                "profile": {
                    "nickname": "nickname",
                    "profile_image_url": "image_url",
                },
            },
        }
        mocked_post.return_value = mock_response

        # 테스트 요청 생성 후, 뷰 호출
        request = self.factory.get("/oauth/kakao/callback", {"code": "fake_code"})
        response = self.view(request)

        # 'message'가 '로그인 완료'인지 확인
        self.assertEqual(response.data["message"], "로그인 완료")


class UserProfileViewTest(TestCase):
    """UserProfileView 뷰에 대한 테스트 케이스"""

    def setUp(self):
        """테스트 케이스의 공통 설정 처리"""
        self.client = APIClient()
        self.user = User.objects.create(
            social_type="kakao",
            social_id="kakao_12345",
            email="user@email.com",
            nickname="user",
        )
        self.client.force_authenticate(user=self.user)

    def test_user_profile(self):
        """UserProfileView 뷰가 정상적으로 회원 정보를 반환하는지 테스트"""
        response = self.client.get(f"/users/{self.user.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nickname"], "user")
        self.assertEqual(response.data["bio"], None)

    def test_user_profile_update(self):
        """UserProfileView 뷰가 정상적으로 회원 정보를 수정하는지 테스트"""
        data = {
            "nickname": "new_nickname",
            "bio": "new_bio",
        }
        response = self.client.patch(f"/users/{self.user.id}", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nickname"], "new_nickname")
        self.assertEqual(response.data["bio"], "new_bio")
        
class FollowingTest(TestCase):
    def setUp(self):
        # 테스트를 위한 유저 생성
        self.client = APIClient()
        self.user = User.objects.create_user(
            "kakao",
            "123456789",
            "test@gmail.com",
            "testuser",
            "testprofileimg",
            "testbio",
            "123456789@",
        )
        # 테스트 클라이언트 인증 방식
        self.client.force_authenticate(user=self.user)

        # 테스트를 위한 다른 유저 생성
        self.user2 = User.objects.create_user(
            "kakao2",
            "1234567892",
            "test2@gmail.com",
            "testuser2",
            "testprofileimg",
            "testbio2",
            "123456789@2",
        )

    # 팔로잉 목록 조회 테스트
    def test_following_list(self):
        # 팔로잉 목록 조회
        response = self.client.get(f"/users/{self.user.id}/following")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 팔로잉 목록 조회 실패 테스트 - 존재하지 않는 유저
    def test_following_list_fail(self):
        # 팔로잉 목록 조회
        response = self.client.get(f"/users/-2/following")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class FollowerTest(TestCase):
    def setUp(self):
        # 테스트를 위한 유저 생성
        self.client = APIClient()
        self.user = User.objects.create_user(
            "kakao",
            "123456789",
            "test@gmail.com",
            "testuser",
            "testprofileimg",
            "testbio",
            "123456789@",
        )
        # 테스트 클라이언트 인증 방식
        self.client.force_authenticate(user=self.user)

        # 테스트를 위한 다른 유저 생성
        self.user2 = User.objects.create_user(
            "kakao2",
            "1234567892",
            "test2@gmail.com",
            "testuser2",
            "testprofileimg",
            "testbio2",
            "123456789@2",
        )

    # 팔로워 목록 조회 테스트
    def test_follower_list(self):
        # 팔로워 데이터 생성
        Follow.objects.create(from_user=self.user2, to_user=self.user)
        # 팔로워 목록 조회
        response = self.client.get(f"/users/{self.user.id}/followers")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 팔로워 목록 조회 실패 테스트 - 존재하지 않는 유저
    def test_follower_list_fail(self):
        # 팔로워 목록 조회
        response = self.client.get(f"/users/-2/followers")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # 팔로워 삭제 테스트
    def test_follower_delete(self):
        # 팔로워 데이터 생성
        Follow.objects.create(from_user=self.user2, to_user=self.user)
        # 팔로워 삭제
        response = self.client.delete(
            f"/users/{self.user.id}/followers", {"follower_user_id": self.user2.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 팔로워 삭제 실패 테스트 - 없는 팔로우 데이터
    def test_follower_delete_fail(self):
        # 팔로워 삭제
        response = self.client.delete(
            f"/users/{self.user.id}/followers", {"follower_user_id": self.user2.id}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class SearchByNicknameTest(TestCase):
    def setUp(self):
        # 테스트를 위한 유저 생성
        self.client = APIClient()
        self.user = User.objects.create_user(
            "kakao",
            "123456789",
            "test@gmail.com",
            "testuser",
            "testprofileimg",
            "testbio",
            "123456789@",
        )
        # 테스트 클라이언트 인증 방식
        self.client.force_authenticate(user=self.user)

        # 닉네임으로 유저 검색 테스트
    def test_search_by_nickname(self):      

        response = self.client.get(f"/users/test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
