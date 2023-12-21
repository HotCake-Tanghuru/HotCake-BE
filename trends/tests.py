from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from .models import Trend, TrendItem
from accounts.models import User, Like, Follow
from trend_missions.models import TrendMission, UserTrendItem


class TrendViewTest(TestCase):
    """핫 트렌드 페이지 조회 테스트"""

    def setUp(self):
        # 테스트를 위한 유저 생성
        self.client = APIClient()
        self.user = User.objects.create(
            social_type="kakao",
            social_id="test_social_id",
            email="testuser@email.com",
            nickname="testuser",
            profile_img="testprofileimg",
        )
        self.client.force_authenticate(user=self.user)

        self.user2 = User.objects.create(
            social_type="kakao",
            social_id="test_social_id2",
            email="testuser2@email.com",
            nickname="testuser2",
            profile_img="testprofileimg",
        )

        # 사용자간 팔로우 관계 생성
        self.follow = Follow.objects.create(
            from_user=self.user,
            to_user=self.user2,
        )

        # 트렌드 생성
        self.trend1 = Trend.objects.create(
            name="test_trend1",
        )
        self.trend2 = Trend.objects.create(
            name="test_trend2",
        )

        # 트렌드 아이템 생성
        self.trend_item1 = TrendItem.objects.create(
            title="test_trend_title1",
            content="test_trend_content1",
            image="test_trend_image1",
        )
        self.trend_item1.trend.set([self.trend1])

        self.trend_item2 = TrendItem.objects.create(
            title="test_trend_title2",
            content="test_trend_content2",
            image="test_trend_image2",
        )
        self.trend_item2.trend.set([self.trend1])

        self.trend_item3 = TrendItem.objects.create(
            title="test_trend_title3",
            content="test_trend_content3",
            image="test_trend_image3",
        )
        self.trend_item3.trend.set([self.trend2])

        # 트렌드 미션 생성
        self.trend_mission = TrendMission.objects.create(
            id=1,
            user=self.user2,
            trend=self.trend1,
        )

        # 사용자 트렌드 아이템 생성
        self.user_trend_item = UserTrendItem.objects.create(
            user=self.user2,
            trend_item=self.trend_item1,
            trend_mission=self.trend_mission,
        )

    # 핫 트렌드 페이지 조회 성공 테스트
    def test_TrendView(self):
        response = self.client.get(f"/trends/")
        self.assertEqual(response.status_code, 200)

    # 팔로우한 유저가 없는 경우 테스트
    def test_TrendView_no_followed_user(self):
        self.follow.delete()
        response = self.client.get(f"/trends/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["followed_trends"], {"message": "아직 팔로우한 친구가 없습니다."}
        )

    # 팔로우한 유저 중 트렌드 인증을 한 유저가 없는 경우 테스트
    def test_TrendView_no_trend_user_trend_item(self):
        self.user_trend_item.delete()
        response = self.client.get(f"/trends/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["followed_trends"], {"message": "아직 트렌드 인증을 한 친구가 없습니다."}
        )


class TrendDetailViewTest(TestCase):
    """트렌드 상세 조회 테스트"""

    def setUp(self):
        # 테스트를 위한 유저 생성
        self.client = APIClient()
        self.user = User.objects.create(
            social_type="kakao",
            social_id="test_social_id",
            email="testuser@email.com",
            nickname="testuser",
            profile_img="testprofileimg",
        )
        self.client.force_authenticate(user=self.user)

        self.user2 = User.objects.create(
            social_type="kakao",
            social_id="test_social_id2",
            email="testuser2@email.com",
            nickname="testuser2",
            profile_img="testprofileimg",
        )

        # 사용자간 팔로우 관계 생성
        self.follow = Follow.objects.create(
            from_user=self.user,
            to_user=self.user2,
        )

        # 트렌드 생성
        self.trend = Trend.objects.create(
            name="test_trend",
        )

        # 트렌드 아이템 생성
        self.trend_item1 = TrendItem.objects.create(
            title="test_trend_title1",
            content="test_trend_content1",
            image="test_trend_image1",
        )
        self.trend_item1.trend.set([self.trend])

        self.trend_item2 = TrendItem.objects.create(
            title="test_trend_title2",
            content="test_trend_content2",
            image="test_trend_image2",
        )
        self.trend_item2.trend.set([self.trend])

        # 트렌드 미션 생성
        self.trend_mission = TrendMission.objects.create(
            id=1,
            user=self.user2,
            trend=self.trend,
        )

    # 트렌드 상세 페이지 조회 성공 테스트
    def test_TrendDetailView(self):
        response = self.client.get(f"/trends/{self.trend.id}/")
        self.assertEqual(response.status_code, 200)

    # 팔로우한 유저가 없는 경우 테스트
    def test_TrendDetailView_no_followed_user(self):
        self.follow.delete()
        response = self.client.get(f"/trends/{self.trend.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["users_with_trend"][0], {"message": "아직 팔로우한 친구가 없습니다."}
        )

    # 팔로우한 유저 중 해당 트렌드 미션에 참여한 유저가 없는 경우 테스트
    def test_TrendDetailView_no_trend_mission(self):
        self.trend_mission.delete()
        response = self.client.get(f"/trends/{self.trend.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["users_with_trend"][0],
            {"message": "아직 트렌드 미션에 참여 중인 친구가 없습니다."},
        )


class TrendLikeViewTest(TestCase):
    """트렌드 좋아요 테스트"""

    def setUp(self):
        # 테스트를 위한 유저 생성
        self.client = APIClient()
        self.user = User.objects.create(
            social_type="kakao",
            social_id="test_social_id",
            email="testuser@email.com",
            nickname="testuser",
            profile_img="testprofileimg",
        )
        self.client.force_authenticate(user=self.user)

        # 트렌드 생성
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

    def setUp(self):
        # 테스트를 위한 유저 생성
        self.client = APIClient()
        self.user = User.objects.create(
            social_type="kakao",
            social_id="test_social_id",
            email="testuser@email.com",
            nickname="testuser",
            profile_img="testprofileimg",
        )
        self.client.force_authenticate(user=self.user)

        # 트렌드 생성
        self.trend1 = Trend.objects.create(
            name="test_trend1",
        )
        self.trend2 = Trend.objects.create(
            name="test_trend2",
        )

        # 트렌드 아이템 생성
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

        # 트렌드 좋아요 생성
        self.like1 = Like.objects.create(
            user=self.user,
            trend=self.trend1,
        )
        self.like2 = Like.objects.create(
            user=self.user,
            trend=self.trend2,
        )

    # 트렌드 좋아요 리스트 조회 성공 테스트
    def test_TrendLikeList(self):
        response = self.client.get(f"/trends/{self.user.id}/likelist/")
        self.assertEqual(response.status_code, 200)

    # 좋아요한 트렌드가 없는 경우 테스트
    def test_TrendLikeList_no_likes(self):
        # 좋아요를 모두 삭제
        self.like1.delete()
        self.like2.delete()

        response = self.client.get(f"/trends/{self.user.id}/likelist/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "아직 좋아요한 트렌드가 없습니다."})
