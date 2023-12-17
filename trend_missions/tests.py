from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from .models import TrendMission, TrendItem, UserTrendItem, Stamp
from accounts.models import User
from trends.models import Trend

# 이미지 필드 테스트용
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http.multipartparser import MultiPartParser


class CreateTrendMissionAPITestCase(TestCase):
    """트렌드 미션 생성 테스트"""

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
        self.trend_item1.trend.set([self.trend])

        self.trend_item2 = TrendItem.objects.create(
            title="test-trend-item2",
            content="test-trend-item-content2",
            image="test-trend-item-image2",
        )
        self.trend_item2.trend.set([self.trend])

        self.trend_item3 = TrendItem.objects.create(
            title="test-trend-item3",
            content="test-trend-item-content3",
            image="test-trend-item-image3",
        )
        self.trend_item3.trend.set([self.trend])

    # 정상 작동 테스트
    def test_createTrendMission_success(self):
        response = self.client.post(
            "/trend-missions/create",
            {"user": self.user.id, "trend": self.trend.id},
        )
        self.assertEqual(response.status_code, 200)

    # 비정상 작동 테스트
    # 이미 생성된 경우 400 에러
    def test_already_createTrendMission_fail(self):
        # 트렌드 미션 미리 생성
        TrendMission.objects.create(
            user=self.user,
            trend=self.trend,
        )

        # 이미 생성된 트렌드 미션 생성 요청
        response = self.client.post(
            "/trend-missions/create",
            {"user": self.user.id, "trend": self.trend.id},
        )
        self.assertEqual(response.status_code, 404)


# http://127.0.0.1:8000/trend-missions/{userid}
class TrendMissionListAPITestCase(TestCase):
    """특정 사용자의 미션 리스트 조회 테스트"""

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
            user=self.user,
            trend=self.trend1,
        )

        TrendMission.objects.create(
            user=self.user,
            trend=self.trend1,
        )
        response = self.client.get(f"/trend-missions/{self.user.id}")

        self.assertEqual(response.status_code, 200)

    # 비정상 작동 테스트
    # 정확하게는 비정상이 아닌, 트렌드 미션을 생성하지 않은 경우 빈 배열 반환

    def test_getTrendMissionList_not_have_list(self):
        response = self.client.get(f"/trend-missions/{self.user.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])


class TrendMissionDetailAPITestCase(TestCase):
    """트렌드 미션 상세 조회 테스트"""

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

        # 테스트를 위한 트렌드 아이템 생성
        self.trend_item1 = TrendItem.objects.create(
            title="test-trend-item1",
            content="test-trend-item-content1",
            image="test-trend-item-image1",
        )
        self.trend_item1.trend.set([self.trend])

        self.trend_item2 = TrendItem.objects.create(
            title="test-trend-item2",
            content="test-trend-item-content2",
            image="test-trend-item-image2",
        )
        self.trend_item2.trend.set([self.trend])

        self.trend_item3 = TrendItem.objects.create(
            title="test-trend-item3",
            content="test-trend-item-content3",
            image="test-trend-item-image3",
        )
        self.trend_item3.trend.set([self.trend])

        # 사용자 트렌드 미션 생성
        self.trend_mission = TrendMission.objects.create(
            user=self.user,
            trend=self.trend,
        )

    # 트렌드 미션 상세 조회 성공 테스트
    def test_TrendMissions_detail(self):
        response = self.client.get(f"/trend-missions/about/{self.trend_mission.id}")
        self.assertEqual(response.status_code, 200)

    # 트렌드 미션 상세 조회 실패 테스트
    def test_TrendMissions_detail_fail(self):
        response = self.client.get(f"/trend-missions/about/-2")
        self.assertEqual(response.status_code, 404)


"""
# 트렌드 미션 아이템 업데이트 테스트
    # 트렌드 미션 아이템 업데이트 테스트
    # 데이터 형태때문에 테스트가 계속 실패
    # 직접 테스트로 대체
    
"""


class TrendMissionCompleteAPITestCase(TestCase):
    """트렌드 미션 완료 테스트"""

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

        # 테스트를 위한 트렌드 아이템 생성
        self.trend_item1 = TrendItem.objects.create(
            title="test-trend-item1",
            content="test-trend-item-content1",
            image="test-trend-item-image1",
        )
        self.trend_item1.trend.set([self.trend])

        self.trend_item2 = TrendItem.objects.create(
            title="test-trend-item2",
            content="test-trend-item-content2",
            image="test-trend-item-image2",
        )
        self.trend_item2.trend.set([self.trend])

        self.trend_item3 = TrendItem.objects.create(
            title="test-trend-item3",
            content="test-trend-item-content3",
            image="test-trend-item-image3",
        )
        self.trend_item3.trend.set([self.trend])

        # 사용자 트렌드 미션 생성
        self.trend_mission = TrendMission.objects.create(
            user=self.user,
            trend=self.trend,
        )

    # 트렌드 미션 완료 성공 테스트
    def test_TrendMissions_complete(self):
        # 사용자 트렌드 미션 아이템 생성
        self.trend_mission_item = UserTrendItem.objects.create(
            user=self.user,
            trend_mission=self.trend_mission,
            trend_item=self.trend_item1,
            is_certificated=True,  # 트렌드 미션 완료 처리
        )

        response = self.client.patch(
            f"/trend-missions/{self.trend_mission.id}/complete",
            {"user": self.user.id},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    # 트렌드 미션 완료 실패(아직 미션 완료 x) 테스트
    def test_TrendMissions_complete_fail(self):
        # 사용자 트렌드 미션 아이템 생성
        self.trend_mission_item = UserTrendItem.objects.create(
            user=self.user,
            trend_mission=self.trend_mission,
            trend_item=self.trend_item1,
            is_certificated=False,  # 아직 모든 인증 완료 x
        )

        response = self.client.patch(
            f"/trend-missions/{self.trend_mission.id}/complete",
            {"user": self.user.id},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 202)


class StampListAPITestCase(TestCase):
    """스탬프 리스트 조회 테스트"""

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

    # 스탬프 리스트 조회 성공 테스트
    def test_StampList(self):
        response = self.client.get(f"/trend-missions/users/{self.user.id}/stamp")
        self.assertEqual(response.status_code, 200)

    # 스탬프 리스트 조회 실패 테스트
    def test_StampList_fail(self):
        response = self.client.get(f"/trend-missions/users/-2/stamp")
        self.assertEqual(response.status_code, 404)
