from django.test import TestCase, Client, RequestFactory
from unittest.mock import patch, MagicMock
from rest_framework import status
from accounts.views import KakaoCallback


class KakaoLoginTest(TestCase):
    """KakaoLogin 뷰에 대한 테스트 케이스입니다."""

    def setUp(self):
        """테스트 케이스의 공통 설정을 처리합니다."""
        self.client = Client()

    def test_kakao_login_redirects(self):
        """KakaoLogin 뷰가 정상적으로 리다이렉트하는지 테스트합니다."""
        header = {"HTTP_Authorization": "access_token"}
        response = self.client.get(
            "/oauth/kakao/login/", content_type="application/json", **header
        )
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)


class KakaoCallbackTest(TestCase):
    """KakaoCallback 뷰에 대한 테스트 케이스입니다."""

    def setUp(self):
        """테스트 케이스의 공통 설정을 처리합니다."""
        self.factory = RequestFactory()
        self.view = KakaoCallback.as_view()

    @patch("requests.post")
    def test_kakao_callback(self, mocked_post):
        """KakaoCallback 뷰가 정상적으로 회원 정보를 반환하는지 테스트합니다."""

        # 가짜 응답을 생성합니다.
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

        request = self.factory.get("/oauth/kakao/callback", {"code": "fake_code"})
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "social_type": "kakao",
                "social_id": "12345",
                "user_email": "user@email.com",
                "user_nickname": "nickname",
                "user_profile_img": "image_url",
            },
        )
