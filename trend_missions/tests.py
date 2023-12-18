from django.test import TestCase, Client
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from django.contrib.auth.models import User
from .models import TrendMission, TrendItem, UserTrendItem, Stamp
from accounts.models import User
from trends.models import Trend

# 이미지 필드 테스트용
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http.multipartparser import MultiPartParser


# 트렌드 미션 페이지 댓글 테스트
class CommentTest(TestCase):
    """트렌드 미션 페이지 댓글 테스트"""
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
            "123456789@"

        )
        # 테스트 클라이언트 인증 방식
        self.client.force_authenticate(user=self.user)

        # 테스트를 위한 트렌드 생성
        self.trend = Trend.objects.create(
            name="test-trend1",
        )

        # 사용자 트렌드 미션 생성
        self.trend_mission = TrendMission.objects.create(
            user=self.user,
            trend=self.trend,
        )

    # 댓글 성공 테스트
    def test_comment_success(self):
        # 댓글 생성
        response = self.client.post(
            f"/trend-missions/1/comments/{self.user.id}",
            {
                "content": "test-comment",
            }
        )
        self.assertEqual(response.status_code, 200)
    
    # 댓글 생성 실패 테스트 (없는 트렌드 미션 페이지)
    def test_comment_fail(self):
        # 댓글 생성
        response = self.client.post(
            f"/trend-missions/-2/comments/{self.user.id}",
            {
                "content": "test-comment",
            }
        )
        self.assertEqual(response.status_code, 404)
