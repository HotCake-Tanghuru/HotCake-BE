from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# serializers
from .serializers import (
    PostTrendMissionsSerializer,
    TrendMissionsSerializer,
    UserTrendItemSerializer,
    UserTrendItemUpdateSerializer,
    StampSerializer,
    CommentSerializer,
)
from accounts.serializers import LikeSerializer

# models
from .models import TrendMission, UserTrendItem, Stamp, Comment
from trends.models import TrendItem, Trend
from accounts.models import User, Like

# swagger
from drf_spectacular.utils import extend_schema


class PostTrendMissionView(APIView):
    """트렌드 인증 미션 생성"""
    @extend_schema(
        methods=["POST"],
        tags=["트렌드 미션"],
        summary="트렌드 미션 생성",
        description="트렌드 미션 페이지를 생성합니다. 해당하는 트렌드 id값을 넣어주세요.",
        request=PostTrendMissionsSerializer,
    )
    def post(self, request):
        # 이미 생성된 트렌드 미션인지 확인
        user = request.user
        if not user:
            return Response("존재하지 않는 사용자입니다.", status=404)
        trend = Trend.objects.get(pk=request.data["trend"])
        if not trend:
            return Response("존재하지 않는 트렌드입니다.", status=404)
        
        if TrendMission.objects.filter(
            user=user, trend=trend
        ).exists():
            return Response("이미 생성된 트렌드 미션입니다.", status=404)
        
        trendMission = TrendMission.objects.create(
            user=user,
            trend=trend,
        )
        serializer = TrendMissionsSerializer(trendMission)

        # 트렌드 미션을 생성하면, 해당하는 트렌드 아이템들을 유저에게 개인적으로 할당
        trend_item_list = TrendItem.objects.filter(trend=trend)

        for trend_item in trend_item_list:
            UserTrendItem.objects.create(
                user=user,
                trend_mission=TrendMission.objects.get(
                    user=user, trend=trend
                ),
                trend_item=trend_item,
            )
        result = serializer.data
        result["trend_item_list"] = trend_item_list.values()
        return Response(result, status=200)


class TrendMissionListView(APIView):
    """사용자의 트렌드 미션 리스트 조회"""
    @extend_schema(
        methods=["GET"],
        tags=["트렌드 미션"],
        summary="트렌드 미션 리스트 조회",
        description="해당하는 사용자의 트렌드 미션 리스트를 조회합니다.",
        request=TrendMissionsSerializer,
    )
    def get(self, request, pk):
        trend_mission = TrendMission.objects.filter(user=pk)
        serializer = TrendMissionsSerializer(trend_mission, many=True)
        data = serializer.data  

        for mission_data in data:
            trend_id = mission_data['trend']
            trend_name = Trend.objects.get(pk=trend_id).name
            mission_data['trend_name'] = trend_name

        return Response(data, status=200)


class TrendMissionDetailView(APIView):
    """트렌드 미션 상세 조회"""
    @extend_schema(
        methods=["GET"],
        tags=["트렌드 미션"],
        summary="트렌드 미션 상세 조회",
        description="트렌드 미션 페이지를 상세 조회합니다. 댓글, 좋아요, 아이템 리스트를 함께 반환합니다.",
    )
    def get(self, request, pk):
        # 트렌드 미션 존재 여부 확인
        if not TrendMission.objects.filter(pk=pk).exists():
            return Response("존재하지 않는 트렌드 미션입니다.", status=404)

        trend_mission = TrendMission.objects.get(pk=pk)
        # 조회수 +1
        serializer = TrendMissionsSerializer(trend_mission)
        serializer.updateViewCount(trend_mission)

        # 트렌드 미션에 해당하는 유저의 트렌드 아이템 리스트 조회
        user_trend_item_list = UserTrendItem.objects.filter(trend_mission=pk)
        result = serializer.data
        result["trend_item_list"] = UserTrendItemSerializer(
            user_trend_item_list, many=True
        ).data

        # 댓글 데이터 조회
        comment_list = Comment.objects.filter(trend_mission=pk)
        result["comment_list"] = CommentSerializer(comment_list, many=True).data

        # 좋아요 데이터 조회
        like_list = Like.objects.filter(trend_mission=pk)
        result["like_list"] = LikeSerializer(like_list, many=True).data

        return Response(result, status=200)


class TrendMissionItemUpdateView(APIView):
    """트렌드 아이템 수정"""
    @extend_schema(
        methods=["PATCH"],
        tags=["트렌드 미션"],
        summary="트렌드 미션 아이템 수정",
        description="트렌드 미션 아이템을 수정합니다. 이미지, 내용을 수정 가능합니다. id에는 트렌드 아이템의 id를 넣어주세요. multipart/form-data 형태로 테스트해주세요.",
        request=UserTrendItemUpdateSerializer,
    )
    def patch(self, request, pk):
        # 트렌드 아이템 소유자 확인
        item = UserTrendItem.objects.get(pk=pk)
        user = request.user
        if item.user != user:
            return Response("트렌드 아이템 소유자가 아니라 수정 권한이 없습니다.", status=404)

        # 트렌드 아이템 수정
        item.is_certificated = True
        serializer = UserTrendItemUpdateSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)


class CheckMissionCompleteView(APIView):
    @extend_schema(
        methods=["PATCH"],
        tags=["트렌드 미션"],
        summary="스탬프 발급받기",
        description="트렌드 미션의 모든 아이템을 완료하면 스탬프를 발급받습니다.",
    )
    def patch(self, request, pk):
        # 트렌드 미션 존재 여부 확인
        if not TrendMission.objects.filter(pk=pk).exists():
            return Response("존재하지 않는 트렌드 미션입니다.", status=404)

        trend_mission = TrendMission.objects.get(pk=pk)
        user = request.user

        # 해당하는 트렌드 미션 아이템 목록 찾기
        trend_item_list = UserTrendItem.objects.filter(trend_mission=pk, user=user)

        # 모든 미션 완수 여부 확인 (인증 여부 확인)
        for trend_item in trend_item_list:
            if trend_item.is_certificated == False:
                return Response("아직 모든 미션을 완료하지 않았습니다.", status=202)

        # 트렌드 미션 상태값 변경 -> True
        trend_mission.is_all_certificated = True
        serializer = TrendMissionsSerializer(trend_mission)
        serializer.updateComplete(trend_mission)

        # 스탬프 발급
        if Stamp.objects.filter(user=user, trend_mission=trend_mission).exists():
            return Response("이미 스탬프를 발급받았습니다.", status=404)

        stamp = Stamp.objects.create(
            user=user,
            trend_mission=trend_mission,
        )

        return Response(serializer.data, status=200)


class StampDetailView(APIView):
    @extend_schema(
        methods=["GET"],
        tags=["트렌드 미션"],
        summary="스탬프 상세조회",
        description="스탬프의 상세 조회 입니다. 스탬프의 id를 넣어주세요.",
    )
    def get(self, request, pk):
        """스탬프 상세 조회"""
        # 스탬프 존재 여부 확인
        if not Stamp.objects.filter(pk=pk).exists():
            return Response("존재하지 않는 스탬프입니다.", status=404)
        # 스탬프 데이터 반환
        stamp = Stamp.objects.get(pk=pk)
        serializer = StampSerializer(stamp)
        result = serializer.data

        # 트렌드 미션 데이터 반환
        trend_mission_id = stamp.trend_mission.id
        trend_mission = TrendMission.objects.get(pk=trend_mission_id)
        result["trend_mission"] = TrendMissionsSerializer(trend_mission).data

        # 트렌드 아이템 데이터 반환
        trend_item_list = UserTrendItem.objects.filter(trend_mission=trend_mission_id)
        result["trend_item_list"] = UserTrendItemSerializer(
            trend_item_list, many=True
        ).data
        return Response(result, status=200)


class StampListView(APIView):
    """스탬프 리스트 조회"""
    @extend_schema(
        methods=["GET"],
        tags=["트렌드 미션"],
        summary="스탬프 리스트 조회",
        description="스탬프의 리스트 조회 입니다. 스탬프 리스트를 조회할 사용자의 id를 넣어주세요.",
    )
    def get(self, request, user_id):
        # 사용자 존재 여부 확인
        if not User.objects.filter(pk=user_id).exists():
            return Response("존재하지 않는 사용자입니다.", status=404)
        # 사용자의 스탬프 리스트 조회
        stamp_list = Stamp.objects.filter(user=user_id)
        serializer = StampSerializer(stamp_list, many=True)
        return Response(serializer.data, status=200)

class CommentUpdateSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    content = serializers.CharField()
class CommentView(APIView):
    """댓글 작성"""
    @extend_schema(
        methods=["POST"],
        tags=["트렌드 미션"],
        summary="댓글 작성",
        description="댓글 작성 페이지입니다. parent_comment값을 제외하고 트렌드 미션의 id와 댓글 내용을 입력해주세요.",
        request=CommentSerializer,
    )
    def post(self, request):
        trend_mission_id = request.data["trend_mission"]
        # 트렌드 미션 존재 여부 확인
        if not TrendMission.objects.filter(pk=trend_mission_id).exists():
            return Response("존재하지 않는 트렌드 미션입니다.", status=404)
        trend_mission = TrendMission.objects.get(pk=trend_mission_id)
        user = request.user
        # 사용자 존재 여부 확인
        if not User.objects.filter(pk=user.id).exists():
            return Response("존재하지 않는 사용자입니다.", status=404)

        # 댓글 작성
        content = request.data["content"]
        comment = Comment.objects.create(
            user=user,
            trend_mission=trend_mission,
            content=content,
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=200)
    
    """댓글 수정"""
    @extend_schema(
        methods=["PATCH"],
        tags=["트렌드 미션"],
        summary="댓글 수정",
        description="댓글 수정 페이지입니다. comment_id값을 추가해서 넣어주세요.",
        request=CommentUpdateSerializer
    )
    def patch(self, request):
        comment_id = request.data["comment_id"]
        
        # 댓글 존재 여부 확인
        if not Comment.objects.filter(pk=comment_id).exists():
            return Response("존재하지 않는 댓글입니다.", status=404)
        comment = Comment.objects.get(pk=comment_id)

        user = request.user
        # 사용자 존재 여부 확인
        if not User.objects.filter(pk=user.id).exists():
            return Response("존재하지 않는 사용자입니다.", status=404)
        # 댓글 작성자 확인
        if comment.user != user:
            return Response("댓글 작성자가 아니라 수정 권한이 없습니다.", status=404)
        # 댓글 수정
        content = request.data["content"]
        comment.content = content
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=200)
    
    """댓글 삭제"""
    @extend_schema(
        methods=["DELETE"],
        tags=["트렌드 미션"],
        summary="댓글 삭제",
        description="댓글 삭제 페이지 입니다. 삭제 요청하는 댓글의 comment_id값을 넣어주세요.",
    )
    def delete(self, request):
        comment_id = request.data["comment_id"]
        # 댓글 존재 여부 확인
        if not Comment.objects.filter(pk=comment_id).exists():
            return Response("존재하지 않는 댓글입니다.", status=404)
        comment = Comment.objects.get(pk=comment_id)
        
        user = request.user
        # 사용자 존재 여부 확인
        if not User.objects.filter(pk=user.id).exists():
            return Response("존재하지 않는 사용자입니다.", status=404)
        # 댓글 작성자 확인
        if comment.user != user:
            return Response("댓글 작성자가 아니라 삭제 권한이 없습니다.", status=404)
        # 댓글 삭제
        comment.delete()
        return Response("댓글이 삭제되었습니다.", status=200)
        
# 대댓글
class CommentReply(APIView):
    """대댓글 작성"""
    @extend_schema(
        methods=["POST"],
        tags=["트렌드 미션"],
        summary="대댓글 작성",
        description="대댓글 작성. comment_id에 댓글 id를 넣고 트렌드 미션의 id와 댓글 내용을 입력해주세요.",
        request=CommentUpdateSerializer,
    )
    def post(self, request, comment_id):
        # 댓글 존재 여부 확인
        if not Comment.objects.filter(pk=comment_id).exists():
            return Response("존재하지 않는 댓글입니다.", status=404)
        comment = Comment.objects.get(pk=comment_id)

        user = request.user
        # 사용자 존재 여부 확인
        if not User.objects.filter(pk=user.id).exists():
            return Response("존재하지 않는 사용자입니다.", status=404)
        
        # 대댓글 작성
        content = request.data["content"]
        reply = Comment.objects.create(
            user=user,
            trend_mission=comment.trend_mission,
            content=content,
            parent_comment=comment,
        )
        serializer = CommentSerializer(reply)
        return Response(serializer.data, status=200)

    """대댓글 수정"""
    @extend_schema(
        methods=["PATCH"],
        tags=["트렌드 미션"],
        summary="대댓글 수정",
        description="대댓글 수정 페이지입니다. comment_id값을 추가해서 넣어주세요.",
        request=CommentUpdateSerializer
    )
    def patch(self, request, comment_id):
        # 대댓글 존재 여부 확인
        if not Comment.objects.filter(pk=comment_id).exists():
            return Response("존재하지 않는 대댓글입니다.", status=404)
        reply = Comment.objects.get(pk=comment_id)

        # 사용자 존재 여부 확인
        user = request.user
        if not User.objects.filter(pk=user.id).exists():
            return Response("존재하지 않는 사용자입니다.", status=404)
        
        # 대댓글 작성자 확인
        if reply.user != user:
            return Response("대댓글 작성자가 아니라 수정 권한이 없습니다.", status=404)
        # 대댓글 수정
        content = request.data["content"]
        reply.content = content
        reply.save()
        serializer = CommentSerializer(reply)
        return Response(serializer.data, status=200)

    """대댓글 삭제"""
    @extend_schema(
        methods=["DELETE"],
        tags=["트렌드 미션"],
        summary="대댓글 삭제",
        description="대댓글 삭제 페이지 입니다. 삭제를 요청하는 댓글의 comment_id값을 넣어주세요.",
    )
    def delete(self, request, comment_id):
        # 대댓글 존재 여부 확인
        if not Comment.objects.filter(pk=comment_id).exists():
            return Response("존재하지 않는 대댓글입니다.", status=404)
        reply = Comment.objects.get(pk=comment_id)


        # 사용자 존재 여부 확인
        user = request.user
        if not User.objects.filter(pk=user.id).exists():
            return Response("존재하지 않는 사용자입니다.", status=404)
        
        # 대댓글 작성자 확인
        if reply.user != user:
            return Response("대댓글 작성자가 아니라 삭제 권한이 없습니다.", status=404)
        # 대댓글 삭제
        reply.delete()
        return Response("대댓글이 삭제되었습니다.", status=200)


class TrendMissionLikeView(APIView):
    """트렌드 미션 좋아요"""
    @extend_schema(
        methods=["PATCH"],
        tags=["트렌드 미션"],
        summary="미션 페이지 좋아요",
        description="미션 페이지에 좋아요를 등록하는 기능입니다. 해당하는 미션페이지의 id값을 넣어주세요.",
    )
    def patch(self, request, trend_mission_id):
        # 트렌드 미션 존재 여부 확인
        if not TrendMission.objects.filter(pk=trend_mission_id).exists():
            return Response("존재하지 않는 트렌드 미션입니다.", status=404)
        trend_mission = TrendMission.objects.get(pk=trend_mission_id)
        """해당하는 좋아요가 이미 있다면 좋아요 취소"""
        # 요청한 사용자가 있는지 확인
        user = request.user
        if not User.objects.filter(pk=user.id).exists():
            return Response("존재하지 않는 사용자입니다.", status=404)

        if Like.objects.filter(user=user, trend_mission=trend_mission).exists():
            like = Like.objects.get(user=user, trend_mission=trend_mission)
            like.delete()
            return Response("좋아요 취소", status=200)

        # 없다면 트렌드 미션 좋아요 처리
        like = Like.objects.create(
            user=user,
            trend_mission=TrendMission.objects.get(pk=trend_mission_id),
        )

        return Response(LikeSerializer(like).data, status=200)
