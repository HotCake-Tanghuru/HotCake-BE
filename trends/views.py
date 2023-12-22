from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Trend, TrendItem
from accounts.models import User, Follow, Like
from trend_missions.models import UserTrendItem, TrendMission

from .serializers import TrendSerializer, TrendItemSerializer, TrendViewCountSerializer
from accounts.serializers import UserSerializer, LikeSerializer

from .serializers import (
    TrendSerializer,
    TrendItemSerializer,
    TrendViewCountSerializer,
    TrendsUserTrendItemSerializer,
)
from accounts.serializers import UserSerializer, LikeSerializer

# swagger
from drf_spectacular.utils import extend_schema

class TrendView(GenericAPIView):
    """핫 트렌드 페이지 조회"""
    @extend_schema(
        methods=["GET"],
        tags=["트렌드"],
        summary="핫 트렌드 페이지 조회",
        description="핫 트렌드 페이지를 조회합니다. ",
    )
    def get(self, request):
        # 핫 트렌드 조회
        trends = Trend.objects.all()
        trend_serializer = TrendSerializer(trends, many=True)

        # 팔로우한 사용자들의 유저 트렌드 아이템 조회
        user = request.user
        follow_list = Follow.objects.filter(from_user=user)
        user_trend_items = {}

        # 가장 최근 업데이트 된 트렌드 미션의 유저 트렌드 아이템 조회
        for follow in follow_list:
            recent_user_trend_item = (
                UserTrendItem.objects.filter(user=follow.to_user)
                .order_by("-updated_at")
                .first()
            )
            if recent_user_trend_item is not None:
                user_trend_item = UserTrendItem.objects.filter(
                    trend_mission=recent_user_trend_item.trend_mission
                )
                user_trend_items[
                    follow.to_user.nickname
                ] = TrendsUserTrendItemSerializer(user_trend_item, many=True).data

        result = {
            "trends": trend_serializer.data,
            "followed_trends": user_trend_items,
        }

        # 팔로우한 유저 여부 확인
        if not follow_list:
            result["followed_trends"] = {"message": "아직 팔로우한 친구가 없습니다."}

        # 팔로우한 유저들의 트렌드 인증 여부 확인
        elif not user_trend_items:
            result["followed_trends"] = {"message": "아직 트렌드 인증을 한 친구가 없습니다."}

        return Response(result, status=200)


class TrendDetailView(GenericAPIView):
    """트렌드 상세 조회"""
    @extend_schema(
        methods=["GET"],
        tags=["트렌드"],
        summary="트렌드 상세 조회",
        description="트렌드 정보를 상세 조회합니다. trend_id값을 넣어 요청합니다. ",
    )
    def get(self, request, trend_id):
        # 페이지 조회수 증가
        trend = get_object_or_404(Trend, id=trend_id)
        trend.view_count += 1
        trend.save()
        trend_view_serializer = TrendViewCountSerializer(trend)

        # 트렌드 아이템 조회
        trend_item = TrendItem.objects.filter(trend=trend_id)
        trend_item_serializer = TrendItemSerializer(trend_item, many=True)

        # 좋아요 데이터 조회
        like_list = Like.objects.filter(trend=trend_id)
        like_list_serializer = LikeSerializer(like_list, many=True)

        # 해당 트렌드에 참여 중인 친구 조회
        user = request.user
        follow_list = Follow.objects.filter(from_user=user)
        users_with_trend = []

        for follow in follow_list:
            trend_missions = TrendMission.objects.filter(
                user=follow.to_user, trend=trend_id
            )
            if trend_missions:
                users_with_trend.append(follow.to_user)

        result = {
            "trend_view_count": trend_view_serializer.data,
            "like_count": like_list.count(),
            "like_list": like_list_serializer.data,
            "trend_item": trend_item_serializer.data,
            "users_with_trend": [],
        }

        # 팔로우한 유저 여부 확인
        if not follow_list:
            result["users_with_trend"].append({"message": "아직 팔로우한 친구가 없습니다."})

        # 팔로우한 유저들의 트렌드 미션 참여 여부 확인
        elif not users_with_trend:
            result["users_with_trend"].append({"message": "아직 트렌드 미션에 참여 중인 친구가 없습니다."})
        else:
            users_serializer = UserSerializer(users_with_trend, many=True)
            result["users_with_trend"] = users_serializer.data

        return Response(result, status=200)


class TrendLikeView(GenericAPIView):
    """트렌드 좋아요"""
    @extend_schema(
        methods=["PATCH"],
        tags=["트렌드"],
        summary="트렌드 좋아요",
        description="해당하는 트렌드에 좋아요를 추가합니다. trend_id값을 넣어 요청합니다. ",
    )
    def patch(self, request, trend_id):
        user = request.user
        trend = get_object_or_404(Trend, id=trend_id)
        like = Like.objects.filter(user=user, trend=trend)

        # 이미 좋아요가 있는 경우 좋아요 취소 처리
        if like.exists():
            like.first().delete()
            trend.save()
            return Response({"message": "좋아요 취소"}, status=200)
        # 좋아요가 없는 경우 좋아요 처리
        else:
            like = Like.objects.create(user=user, trend=trend)
            trend.save()

            return Response(LikeSerializer(like).data, status=200)


class TrendLikeListView(GenericAPIView):
    """사용자가 좋아요한 트렌드 목록 조회"""
    @extend_schema(
        methods=["GET"],
        tags=["트렌드"],
        summary="트렌드 목록 조회",
        description="사용자의 트렌드 목록을 조회합니다. 사용자의 user_id값을 넣어 요청합니다. ",
    )
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        user_like_list = Like.objects.filter(user=user)

        # 아직 좋아요한 트렌드가 없는 경우
        if not user_like_list:
            return Response({"message": "아직 좋아요한 트렌드가 없습니다."}, status=200)

        liked_trend_id = user_like_list.values_list("trend_id", flat=True)

        trends = Trend.objects.filter(id__in=liked_trend_id)
        trend_serializer = TrendSerializer(trends, many=True)
        result = trend_serializer.data

        for trend in result:
            trend_items = TrendItem.objects.filter(trend__id=trend["id"])
            trend["trend_item"] = TrendItemSerializer(trend_items, many=True).data

        return Response(result, status=200)
