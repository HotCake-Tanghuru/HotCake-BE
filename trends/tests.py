from django.test import TestCase
from rest_framework.test import APIClient
from accounts.models import User
from django.contrib.auth.models import User
from .models import Trend, TrendItem
from accounts.models import User, Like
from .serializers import TrendSerializer, TrendItemSerializer


class TrendLikeViewTest(TestCase):
    """트렌드 좋아요 테스트"""

    # 테스트를 위한 유저 생성
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            social_type="kakao",
            social_id="test_social_id",
            email="testuser@email.com",
            nickname="testuser",
            profile_img="testprofileimg",
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


class TrendLikeListViewTest(TestCase):
    """사용자가 좋아요한 트렌드 목록 조회 테스트"""

    # 테스트를 위한 유저 생성
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            social_type="kakao",
            social_id="test_social_id",
            email="testuser@email.com",
            nickname="testuser",
            profile_img="testprofileimg",
        )
        self.client.force_authenticate(user=self.user)

        # 테스트를 위한 트렌드 생성
        self.trend1 = Trend.objects.create(
            name="test_trend1",
        )
        self.trend2 = Trend.objects.create(
            name="test_trend2",
        )

        # 테스트를 위한 트렌드 아이템 생성
        self.trend_item1 = TrendItem.objects.create(
            title="test_trend1_title",
            content="test_trend1_content",
            image="test_trend1_image",
        )
        self.trend_item1.trend.set([self.trend1])

        self.trend_item2 = TrendItem.objects.create(
            title="test_trend2_title",
            content="test_trend2_content",
            image="test_trend2_image",
        )
        self.trend_item2.trend.set([self.trend1])

        self.trend_item3 = TrendItem.objects.create(
            title="test_trend3_title",
            content="test_trend3_content",
            image="test_trend3_image",
        )
        self.trend_item3.trend.set([self.trend2])

        # 테스트를 위한 트렌드 좋아요 생성
        self.like1 = Like.objects.create(
            user=self.user,
            trend=self.trend1,
        )
        self.like2 = Like.objects.create(
            user=self.user,
            trend=self.trend2,
        )

    def test_TrendLikeList(self):
        # 트렌드 좋아요 리스트 조회 성공 테스트
        response = self.client.get(f"/trends/{self.user.id}/likelist/")
        trends = Trend.objects.filter(
            id__in=Like.objects.filter(user=self.user).values_list(
                "trend_id", flat=True
            )
        )
        trend_serializer = TrendSerializer(trends, many=True)
        expected_data = trend_serializer.data

        for trend in expected_data:
            trend_items = TrendItem.objects.filter(trend__id=trend["id"])
            trend["trend_item"] = TrendItemSerializer(trend_items, many=True).data

        self.assertEqual(response.data, expected_data)
        self.assertEqual(response.status_code, 200)
