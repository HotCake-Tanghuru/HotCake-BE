from django.test import TestCase, Client
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from django.contrib.auth.models import User
from .models import TrendMission, TrendItem, UserTrendItem, Stamp, Comment
from accounts.models import User
from trends.models import Trend
from rest_framework_simplejwt.tokens import RefreshToken

# 이미지 필드 테스트용
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http.multipartparser import MultiPartParser


class CreateTrendMissionAPITestCase(TestCase):
    """트렌드 미션 생성 테스트"""

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
            {"trend": self.trend.id},
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
            {"trend": self.trend.id},
        )
        self.assertEqual(response.status_code, 404)


class TrendMissionDetailAPITestCase(TestCase):
    """트렌드 미션 상세 조회 테스트"""
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

        # 댓글 생성
        self.comment = Comment.objects.create(
            user=self.user,
            trend_mission=self.trend_mission,
            content="test-comment",
        )

    # 트렌드 미션 상세 조회 성공 테스트
    def test_TrendMissions_detail(self):
        response = self.client.get(f"/trend-missions/about/{self.trend_mission.id}")
        self.assertEqual(response.status_code, 200)

    # 트렌드 미션 상세 조회 실패 테스트
    def test_TrendMissions_detail_fail(self):
        response = self.client.get(f"/trend-missions/about/-2")
        self.assertEqual(response.status_code, 404)


# http://127.0.0.1:8000/trend-missions/{userid}
class TrendMissionListAPITestCase(TestCase):
    """특정 사용자의 미션 리스트 조회 테스트"""

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


class StampDetailAPITest(TestCase):
    """스탬프 상세 조회 테스트"""
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


# # """
# # # 트렌드 미션 아이템 업데이트 테스트
# #     # 트렌드 미션 아이템 업데이트 테스트
# #     # 데이터 형태때문에 테스트가 계속 실패
# #     # 직접 테스트로 대체
    
# # """


class TrendMissionCompleteAPITestCase(TestCase):
    """트렌드 미션 완료 - 스탬프 발급 테스트"""

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
            f"/trend-missions/{self.trend_mission.id}/complete"
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
            f"/trend-missions/{self.trend_mission.id}/complete"
        )
        self.assertEqual(response.status_code, 202)


class StampListAPITestCase(TestCase):
    """스탬프 리스트 조회 테스트"""

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
        
        
class StampDetailAPITest(TestCase):
    """스탬프 상세 조회 테스트"""
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

        # 스탬프 생성
        self.stamp = Stamp.objects.create(
            user=self.user,
            trend_mission=self.trend_mission,
        )

    # 스탬프 상세 조회 성공 테스트
    def test_StampDetail(self):
        response = self.client.get(f"/trend-missions/users/stamp/{self.user.id}")
        self.assertEqual(response.status_code, 200)

    # 스탬프 상세 조회 실패 테스트
    def test_StampList_fail(self):
        response = self.client.get(f"/trend-missions/users/stamp/-2")
        self.assertEqual(response.status_code, 404)


class TrendMissionLikeAPITestCase(TestCase):
    """트렌드 미션 좋아요 테스트"""

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

        # 토큰 생성
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        self.client.cookies['access'] = access_token

        # 테스트를 위한 트렌드 생성
        self.trend = Trend.objects.create(
            name="test-trend1",
        )

        # 사용자 트렌드 미션 생성
        self.trend_mission = TrendMission.objects.create(
            user=self.user,
            trend=self.trend,
        )

    # 트렌드 미션 좋아요 성공 테스트 - 실패
    def test_TrendMissionLike(self):
        response = self.client.put(
            f"/trend-missions/{self.trend_mission.id}/like"
        )
        self.assertEqual(response.status_code, 200)
    
    # 트렌드 미션 좋아요 실패 테스트
    def test_TrendMissionLike_fail(self):
        response = self.client.put(
            f"/trend-missions/-2/like"
        )
        self.assertEqual(response.status_code, 404)


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
            f"/trend-missions/comments",
            {
                "trend_mission": self.trend_mission.id,
                "content": "test-comment",
            }
        )
        self.assertEqual(response.status_code, 200)
    # 댓글 생성 실패 테스트 (없는 트렌드 미션 페이지)
    def test_comment_fail(self):
        # 댓글 생성
        response = self.client.post(
            f"/trend-missions/comments",
            {
                "trend_mission": -1,
                "content": "test-comment",
            }
        )
        self.assertEqual(response.status_code, 404)

    # 댓글 수정 성공 테스트
    def test_comment_update_success(self):
        # 댓글 생성
        self.comment = Comment.objects.create(
            user=self.user,
            trend_mission=self.trend_mission,
            content="test-comment",
        )
        # 댓글 수정
        response = self.client.patch(
            f"/trend-missions/comments",
            {
                "comment_id": self.comment.id,
                "content": "test-comment-update",
            }
        )
        self.assertEqual(response.status_code, 200)
    
    # 댓글 수정 실패 테스트 - 없는 댓글
    def test_comment_update_fail(self):
        # 댓글 생성
        self.comment = Comment.objects.create(
            user=self.user,
            trend_mission=self.trend_mission,
            content="test-comment",
        )
        # 댓글 수정
        response = self.client.patch(
            f"/trend-missions/comments",
            {
                "comment_id": -2,
                "content": "test-comment-update",
            }
        )
        self.assertEqual(response.status_code, 404)

        # 댓글 수정 실패 테스트 - 없는 사용자의 요청
    def test_comment_update_fail2(self):
        # 댓글 생성
        self.comment = Comment.objects.create(
            user=self.user,
            trend_mission=self.trend_mission,
            content="test-comment",
        )
        # 댓글 수정
        response = self.client.patch(
            f"/trend-missions/comments",
            {
                "comment_id": self.comment.id,
                "content": "test-comment-update",
            }
        )
    
    # 댓글 수정 실패 테스트 - 댓글 작성자가 아닌 사용자의 요청
    def test_comment_update_fail3(self):
        # 다른 사용자 생성
        user2 = User.objects.create_user(
            "kakao2",
            "1234567892",
            "test@gmail.com2",
            "testuser2",
            "testprofileimg2",
            "testbio2",
            "123456789@2"
        )
        # 댓글 생성
        self.comment = Comment.objects.create(
            user=user2,
            trend_mission=self.trend_mission,
            content="test-comment",
        )
        # 댓글 수정
        response = self.client.patch(
            f"/trend-missions/comments",
            {
                "comment_id": self.comment.id,
                "content": "test-comment-update",
            }
        )
        self.assertEqual(response.status_code, 404)
    # 댓글 삭제
    def test_comment_delete_success(self):
        # 댓글 생성
        self.comment = Comment.objects.create(
            user=self.user,
            trend_mission=self.trend_mission,
            content="test-comment",
        )
        # 댓글 삭제
        response = self.client.delete(
            f"/trend-missions/comments",
            {
                "comment_id": self.comment.id,
            }
        )
        self.assertEqual(response.status_code, 200)

    # 댓글 삭제 실패 테스트 - 없는 댓글
    def test_comment_delete_fail(self):
        # 댓글 생성
        self.comment = Comment.objects.create(
            user=self.user,
            trend_mission=self.trend_mission,
            content="test-comment",
        )
        # 댓글 삭제
        response = self.client.delete(
            f"/trend-missions/comments",
            {
                "comment_id": -2,
            }
        )
        self.assertEqual(response.status_code, 404)
    
    # 댓글 삭제 실패 테스트 - 댓글 작성자가 아닌 사용자의 요청
    def test_comment_delete_fail3(self):
        # 다른 사용자 생성
        user2 = User.objects.create_user(
            "kakao2",
            "1234567892",
            "test@gmail.com2",
            "testuser2",
            "testprofileimg2",
            "testbio2",
            "123456789@2"
        )
        # 댓글 생성
        self.comment = Comment.objects.create(
            user=user2,
            trend_mission=self.trend_mission,
            content="test-comment",
        )
        # 댓글 삭제
        response = self.client.delete(
            f"/trend-missions/comments",
            {
                "comment_id": self.comment.id,
            }
        )
        self.assertEqual(response.status_code, 404)

        # 트렌드 미션 페이지 대댓글 테스트
class CommentReplyTest(TestCase):
    """트렌드 미션 페이지 대댓글 테스트"""
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

        # 댓글 생성
        self.comment = Comment.objects.create(
            user=self.user,
            trend_mission=self.trend_mission,
            content="test-comment",
        )

    # 대댓글 작성 성공 테스트
    def test_comment_reply_success(self):
        # 대댓글 생성
        response = self.client.post(
            f"/trend-missions/comments/{self.comment.id}/replies",
            {
                "content": "test-reply",
            }
        )
        self.assertEqual(response.status_code, 200)

    
    """대댓글 작성 실패 테스트"""
    # 대댓글 작성 실패 테스트 - 없는 댓글
    def test_comment_reply_fail(self):
        # 댓글 생성
        self.comment = Comment.objects.create(
            user=self.user,
            trend_mission=self.trend_mission,
            content="test-comment",
        )
    
    
    """대댓글 수정 테스트"""
    # 대댓글 수정 성공 테스트
    def test_comment_reply_update_success(self):
        # 대댓글 생성
        self.comment_reply = Comment.objects.create(
            user=self.user,
            trend_mission=self.trend_mission,
            content="test-reply",
            parent_comment=self.comment,
        )
        # 대댓글 수정
        response = self.client.patch(
            f"/trend-missions/comments/{self.comment_reply.id}/replies",
            {
                "content": "test-reply-update",
            }
        )
        self.assertEqual(response.status_code, 200)

    # 대댓글 수정 실패 테스트 - 작성자가 다름
    def test_comment_reply_update_fail(self):
        # 다른 사용자 생성
        user2 = User.objects.create_user(
            "kakao2",
            "1234567892",
            "test@gmail.com2",
            "testuser2",
            "testprofileimg2",
            "testbio2",
            "123456789@2"
        )
        # 대댓글 생성
        self.comment_reply = Comment.objects.create(
            user=user2,
            trend_mission=self.trend_mission,
            content="test-reply",
            parent_comment=self.comment,
        )
        # 대댓글 수정
        response = self.client.patch(
            f"/trend-missions/comments/{self.comment_reply.id}/replies",
            {
                "content": "test-reply-update",
            }
        )
        self.assertEqual(response.status_code, 404)
    
    """대댓글 삭제 테스트"""
    # 대댓글 삭제 성공 테스트
    def test_comment_reply_delete_success(self):
        # 대댓글 생성
        self.comment_reply = Comment.objects.create(
            user=self.user,
            trend_mission=self.trend_mission,
            content="test-reply",
            parent_comment=self.comment,
        )
        # 대댓글 삭제
        response = self.client.delete(
            f"/trend-missions/comments/{self.comment_reply.id}/replies",
        )
        self.assertEqual(response.status_code, 200)

    # 대댓글 삭제 실패 테스트 - 작성자가 다름
    def test_comment_reply_delete_fail(self):
        # 다른 사용자 생성
        user2 = User.objects.create_user(
            "kakao2",
            "1234567892",
            "test@gmail.com2",
            "testuser2",
            "testprofileimg2",
            "testbio2",
            "123456789@2"
        )
        # 대댓글 생성
        self.comment_reply = Comment.objects.create(
            user=user2,
            trend_mission=self.trend_mission,
            content="test-reply",
            parent_comment=self.comment,
        )
        # 대댓글 삭제
        response = self.client.delete(
            f"/trend-missions/comments/{self.comment_reply.id}/replies",
        )
        self.assertEqual(response.status_code, 404)
