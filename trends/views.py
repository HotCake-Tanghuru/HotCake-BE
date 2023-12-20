from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Trend, TrendItem
from accounts.models import Follow
from trend_missions.models import UserTrendItem

from .serializers import (
    TrendSerializer,
    TrendItemSerializer,
    TrendViewCountSerializer,
    TrendsUserTrendItemSerializer,
)
from accounts.serializers import UserSerializer


class TrendView(GenericAPIView):
    """핫 트렌드 페이지 조회"""

    def get(self, request):
        # 핫 트렌드 조회
        trends = Trend.objects.all()
        trend_serializer = TrendSerializer(trends, many=True)

        # 팔로우한 사용자들의 트렌드 아이템 조회
        user = request.user
        follow_list = Follow.objects.filter(from_user=user)
        user_trend_items = {}

        # 가장 최근 업데이트 된 트렌드 미션의 트렌드 아이템 조회
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

        # 팔로우한 유저들의 트렌드 참여 여부 확인
        elif not user_trend_items:
            result["followed_trends"] = {"message": "아직 트렌드에 참여 중인 친구가 없습니다."}

        return Response(result, status=200)


class TrendDetailView(GenericAPIView):
    """트렌드 상세 조회"""

    def get(self, request, trend_id):
        # 페이지 조회수 증가
        trend = get_object_or_404(Trend, id=trend_id)
        trend.view_count += 1
        trend.save()
        trend_view_serializer = TrendViewCountSerializer(trend)

        # 트렌드 아이템 조회
        trend_item = TrendItem.objects.filter(trend=trend_id)
        trend_item_serializer = TrendItemSerializer(trend_item, many=True)

        # 해당 트렌드에 참여 중인 친구 조회
        user = request.user
        follow_list = Follow.objects.filter(from_user=user)
        users_with_trend = []

        for follow in follow_list:
            user_trend_items = UserTrendItem.objects.filter(
                user=follow.to_user, trend_item__trend=trend_id
            )
            if user_trend_items:
                users_with_trend.append(follow.to_user)

        result = {
            "trend_view_count": trend_view_serializer.data,
            "trend_item": trend_item_serializer.data,
            "users_with_trend": [],
        }

        # 팔로우한 유저 여부 확인
        if not follow_list:
            result["users_with_trend"].append({"message": "아직 팔로우한 친구가 없습니다."})

        # 팔로우한 유저들의 트렌드 참여 여부 확인
        elif not users_with_trend:
            result["users_with_trend"].append({"message": "아직 트렌드에 참여 중인 친구가 없습니다."})
        else:
            users_serializer = UserSerializer(users_with_trend, many=True)
            result["users_with_trend"] = users_serializer.data

        return Response(result, status=200)
