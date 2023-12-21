from django.test import TestCase, Client, RequestFactory
from unittest.mock import patch, MagicMock
from rest_framework import status
from rest_framework.test import APIClient
from accounts.views import KakaoCallback
from accounts.models import User


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
