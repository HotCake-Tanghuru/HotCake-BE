from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import TrendMission, TrendItem
from accounts.models import User
from trends.models import Trend

# 미션 페이지 생성 테스트
class CreateTrendMissionAPITestCase(TestCase):
    def setUp(self):
        # 테스트를 위한 유저 생성
        self.client = Client()
        self.user = User.objects.create_user(
            "testuser", "testemail@test.com", "123456789@"
        )

        # 테스트를 위한 트렌드 생성
        self.trend = Trend.objects.create(
            name="test-trend",
        )

        # 테스트를 위한 트렌드 아이템 생성
        self.trend_item1 = TrendItem.objects.create(
            title="test-trend-item1",
            content="test-trend-item-content1",
            image="test-trend-item-image1",
        )
        self.trend_item1.trend_id.set([self.trend])

        self.trend_item2 = TrendItem.objects.create(
            title="test-trend-item2",
            content="test-trend-item-content2",
            image="test-trend-item-image2",
        )
        self.trend_item2.trend_id.set([self.trend])

        self.trend_item3 = TrendItem.objects.create(
            title="test-trend-item3",
            content="test-trend-item-content3",
            image="test-trend-item-image3",
        )
        self.trend_item3.trend_id.set([self.trend])

    # 정상 작동 테스트  
    def test_createTrendMission_success(self):
        response = self.client.post(
            "/trend-missions/create",
            {"user_id": self.user.id, "trend_id": self.trend.id},
        )
        self.assertEqual(response.status_code, 200)

    # 비정상 작동 테스트
    # 이미 생성된 경우 400 에러
    def test_already_createTrendMission_fail(self):
        
        # 트렌드 미션 미리 생성
        TrendMission.objects.create(
            user_id=self.user,
            trend_id=self.trend,
        )

        # 이미 생성된 트렌드 미션 생성 요청
        response = self.client.post(
            "/trend-missions/create",
            {"user_id": self.user.id, "trend_id": self.trend.id},
        )
        self.assertEqual(response.status_code, 404)


# 특정 사용자의 미션 리스트 조회 테스트
# http://127.0.0.1:8000/trend-missions/{userid}

class TrendMissionListAPITestCase(TestCase):
    def setUp(self):
        # 테스트를 위한 유저 생성
        self.client = Client()
        self.user = User.objects.create_user(
            "testuser", "testemail@test.com", "123456789@"
        )

        # 테스트를 위한 트렌드 생성
        self.trend1 = Trend.objects.create(
            name="test-trend1",
        )

        self.trend2 = Trend.objects.create(
            name="test-trend2",
        )
    
    # 정상 작동 테스트
    def test_getTrendMissionList_success(self):
        # 트렌드 미션 미리 생성
        TrendMission.objects.create(
            user_id=self.user,
            trend_id=self.trend1,
        )

        TrendMission.objects.create(
            user_id=self.user,
            trend_id=self.trend1,
        )
        response = self.client.get(f"/trend-missions/{self.user.id}")

        self.assertEqual(response.status_code, 200)
    
    # 비정상 작동 테스트
    # 정확하게는 비정상이 아닌, 트렌드 미션을 생성하지 않은 경우 빈 배열 반환

    def test_getTrendMissionList_not_have_list(self):
        response = self.client.get(f"/trend-missions/{self.user.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

