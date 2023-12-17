from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from .models import TrendMission, TrendItem, UserTrendItem, Stamp
from accounts.models import User
from trends.models import Trend

# 이미지 필드 테스트용
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http.multipartparser import MultiPartParser




class StampDetailAPITest(TestCase):
    """스탬프 상세 조회 테스트"""
    def setUp(self):
        # 테스트를 위한 유저 생성
        self.client = Client()
        self.user = User.objects.create_user(
            "testuser", "testemail@test.com", "123456789@"
        )

        # 테스트를 위한 트렌드 생성
        self.trend = Trend.objects.create(
            name="test-trend1",
        )

        # 사용자 트렌드 미션 생성
        self.trend_mission = TrendMission.objects.create(
            user=self.user,
            trend=self.trend,
        )

        # 스탬프 생성
        self.stamp = Stamp.objects.create(
            user=self.user,
            trend_mission=self.trend_mission,
        )

    # 스탬프 상세 조회 성공 테스트
    def test_StampDetail(self):
        response = self.client.get(f"/trend-missions/users/stamp/{self.user.id}")
        self.assertEqual(response.status_code, 200)

    # 스탬프 리스트 조회 실패 테스트
    def test_StampList_fail(self):
        response = self.client.get(f"/trend-missions/users/stamp/-2")
        self.assertEqual(response.status_code, 404)