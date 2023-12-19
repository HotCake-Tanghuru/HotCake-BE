from django.shortcuts import render, get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Trend, TrendItem
from accounts.models import User, Follow
from trend_missions.models import UserTrendItem, TrendMission

from .serializers import TrendSerializer, TrendItemSerializer, TrendViewCountSerializer
from trend_missions.serializers import UserTrendItemSerializer
from accounts.serializers import UserSerializer


class TrendView(GenericAPIView):
    """핫 트렌드 페이지 조회"""

    def get(self, request):
        # 트렌드 조회
        trends = Trend.objects.all()
        trend_serializer = TrendSerializer(trends, many=True)

        # 팔로우한 사용자들의 트렌드 아이템 조회
        user = request.user
        follow_list = Follow.objects.filter(from_user=user)
        user_trend_item_list = []

        for follow in follow_list:
            user_trend_items = UserTrendItem.objects.filter(user=follow.to_user)
            user_trend_item_list.extend(user_trend_items)

        result = {
            "trends": trend_serializer.data,
            "followed_trends": [],
        }

        # 팔로우한 유저 여부 확인
        if not follow_list:
            result["followed_trends"].append({"message":"아직 팔로우한 친구가 없습니다."})

        # 팔로우한 유저들의 트렌드 참여 여부 확인
        elif not user_trend_item_list:
            result["followed_trends"].append({"message": "아직 트렌드에 참여 중인 친구가 없습니다."})
        else:
            trend_item_serializer = UserTrendItemSerializer(
                user_trend_item_list, many=True
            )
            result["followed_trends"].extend(trend_item_serializer.data)

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
            result["users_with_trend"].append({"message":"아직 팔로우한 친구가 없습니다."})

        # 팔로우한 유저들의 트렌드 참여 여부 확인
        elif not users_with_trend:
            result["users_with_trend"].append({"message":"아직 트렌드에 참여 중인 친구가 없습니다."})
        else:
            users_serializer = UserSerializer(users_with_trend, many=True)
            result["users_with_trend"] = users_serializer.data

        return Response(result, status=200)
