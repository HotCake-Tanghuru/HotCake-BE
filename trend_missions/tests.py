from django.test import TestCase, Client
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from django.contrib.auth.models import User
from .models import TrendMission, TrendItem, UserTrendItem, Stamp, Comment
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

    # 댓글 수정 성공 테스트
    def test_comment_update_success(self):
        # 댓글 생성
        response = self.client.post(
            f"/trend-missions/1/comments/{self.user.id}",
            {
                "content": "test-comment",
            }
        )
        # 댓글 수정
        response = self.client.patch(
            f"/trend-missions/comments/1/{self.user.id}",
            {
                "content": "test-comment-update",
            }
        )
        self.assertEqual(response.status_code, 200)
    
    # 댓글 수정 실패 테스트 - 없는 댓글
    def test_comment_update_fail(self):
        # 댓글 생성
        response = self.client.post(
            f"/trend-missions/1/comments/{self.user.id}",
            {
                "content": "test-comment",
            }
        )
        # 댓글 수정
        response = self.client.patch(
            f"/trend-missions/comments/-2/{self.user.id}",
            {
                "content": "test-comment-update",
            }
        )
        self.assertEqual(response.status_code, 404)

    # 댓글 수정 실패 테스트 - 없는 사용자의 요청
    def test_comment_update_fail2(self):
        # 댓글 생성
        response = self.client.post(
            f"/trend-missions/1/comments/{self.user.id}",
            {
                "content": "test-comment",
            }
        )
        # 댓글 수정
        response = self.client.patch(
            f"/trend-missions/comments/1/-2",
            {
                "content": "test-comment-update",
            }
        )
        self.assertEqual(response.status_code, 404)
    
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
        response = self.client.post(
            f"/trend-missions/1/comments/{self.user.id}",
            {
                "content": "test-comment",
            }
        )
        # 댓글 수정
        response = self.client.patch(
            f"/trend-missions/comments/1/{user2.id}",
            {
                "content": "test-comment-update",
            }
        )
        self.assertEqual(response.status_code, 404)
    # 댓글 삭제
    def test_comment_delete_success(self):
        # 댓글 생성
        response = self.client.post(
            f"/trend-missions/1/comments/{self.user.id}",
            {
                "content": "test-comment",
            }
        )
        # 댓글 삭제
        response = self.client.delete(
            f"/trend-missions/comments/1/{self.user.id}",
        )
        self.assertEqual(response.status_code, 200)

    # 댓글 삭제 실패 테스트 - 없는 댓글
    def test_comment_delete_fail(self):
        # 댓글 생성
        response = self.client.post(
            f"/trend-missions/1/comments/{self.user.id}",
            {
                "content": "test-comment",
            }
        )
        # 댓글 삭제
        response = self.client.delete(
            f"/trend-missions/comments/-2/{self.user.id}",
        )
        self.assertEqual(response.status_code, 404)
    
    # 댓글 삭제 실패 테스트 - 없는 사용자의 요청
    def test_comment_delete_fail2(self):
        # 댓글 생성
        response = self.client.post(
            f"/trend-missions/1/comments/{self.user.id}",
            {
                "content": "test-comment",
            }
        )
        # 댓글 삭제
        response = self.client.delete(
            f"/trend-missions/comments/1/-2",
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
        response = self.client.post(
            f"/trend-missions/1/comments/{self.user.id}",
            {
                "content": "test-comment",
            }
        )
        # 댓글 삭제
        response = self.client.delete(
            f"/trend-missions/comments/1/{user2.id}",
        )
        self.assertEqual(response.status_code, 404)


# 트렌드 미션 페이지 대댓글 테스트
class CommentReplyTest(TestCase):
    """트렌드 미션 페이지 대댓글 테스트"""
    def setUp(self):
        # 테스트를 위한 유저 생성
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
            f"/trend-missions/comments/{self.comment.id}/replies/{self.user.id}",
            {
                "content": "test-reply",
            }
        )
        self.assertEqual(response.status_code, 200)
    
    """대댓글 작성 실패 테스트"""
    # 대댓글 작성 실패 테스트 - 없는 댓글
    def test_comment_reply_fail(self):
        # 대댓글 생성
        response = self.client.post(
            f"/trend-missions/comments/-2/replies/{self.user.id}",
            {
                "content": "test-reply",
            }
        )
        self.assertEqual(response.status_code, 404)
    
    # 대댓글 작성 실패 테스트 - 없는 사용자의 요청
    def test_comment_reply_fail2(self):
        # 대댓글 생성
        response = self.client.post(
            f"/trend-missions/comments/{self.comment.id}/replies/-2",
            {
                "content": "test-reply",
            }
        )
        self.assertEqual(response.status_code, 404)
    
    """대댓글 수정 테스트"""
    # 대댓글 수정 성공 테스트
    def test_comment_reply_update_success(self):
        # 대댓글 생성
        response = self.client.post(
            f"/trend-missions/comments/{self.comment.id}/replies/{self.user.id}",
            {
                "content": "test-reply",
            }
        )
        # 대댓글 생성
        self.comment_reply = Comment.objects.create(
            user=self.user,
            trend_mission=self.trend_mission,
            content="test-reply",
            parent_comment=self.comment,
        )
        # 대댓글 수정
        response = self.client.patch(
            f"/trend-missions/comments/{self.comment_reply.id}/replies/{self.user.id}",
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
            user=self.user,
            trend_mission=self.trend_mission,
            content="test-reply",
            parent_comment=self.comment,
        )
        # 대댓글 수정
        response = self.client.patch(
            f"/trend-missions/comments/{self.comment_reply.id}/replies/-2",
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
            f"/trend-missions/comments/{self.comment_reply.id}/replies/{self.user.id}",
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
            user=self.user,
            trend_mission=self.trend_mission,
            content="test-reply",
            parent_comment=self.comment,
        )
        # 대댓글 삭제
        response = self.client.delete(
            f"/trend-missions/comments/{self.comment_reply.id}/replies/-2",
        )
        self.assertEqual(response.status_code, 404)
        