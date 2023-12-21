from django.test import TestCase
from rest_framework.test import APIClient

from .models import Trend
from accounts.models import User


class TrendLikeViewTest(TestCase):
    """트렌드 좋아요 테스트"""

    # 테스트를 위한 유저 생성
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            social_type="kakao",
            social_id="kakao_12345",
            email="user@email.com",
            nickname="user",
        )
        self.client.force_authenticate(user=self.user)

        # 테스트를 위한 트렌드 생성
        self.trend = Trend.objects.create(
            name="test_trend",
        )

    def test_TrendLike(self):
        # 트렌드 좋아요 성공 테스트
        response = self.client.patch(f"/trends/{self.trend.id}/likes/")
        self.assertEqual(response.status_code, 200)

        # 트렌드 좋아요 취소 성공 테스트
        response = self.client.patch(f"/trends/{self.trend.id}/likes/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "좋아요 취소")
