from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView

# serializers
from .serializers import PostTrendMissionsSerializer, TrendMissionsSerializer

# models
from .models import TrendMission, UserTrendItem, Stamp
from trends.models import TrendItem, Trend
from accounts.models import User


class PostTrendMissionView(GenericAPIView):
    # 트렌드 인증 미션 생성
    def post(self, request):
        # 이미 생성된 트렌드 미션인지 확인
        if TrendMission.objects.filter(
            user_id=request.data["user_id"], trend_id=request.data["trend_id"]
        ).exists():
            return Response("이미 생성된 트렌드 미션입니다.", status=404)

        serializer = PostTrendMissionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # 트렌드 미션을 생성하면, 해당하는 트렌드 아이템들을 유저에게 개인적으로 할당
            trend = request.data["trend_id"]
            trend_item_list = TrendItem.objects.filter(trend_id=trend)

            for trend_item in trend_item_list:
                UserTrendItem.objects.create(
                    user_id=User.objects.get(pk=request.data["user_id"]),
                    trend_mission_id=TrendMission.objects.get(
                        user_id=request.data["user_id"], trend_id=trend
                    ),
                    trend_item_id=trend_item,
                )
            result = serializer.data
            result["trend_item_list"] = trend_item_list.values()  # 트렌드 아이템도 담아서 전달
            return Response(result, status=200)
        return Response(serializer.errors)
    
class TrendMissionListView(GenericAPIView):
    # 사용자의 트렌드 미션 리스트 조회
    def get(self, request, pk):
        trend_mission = TrendMission.objects.filter(user_id=pk)
        serializer = TrendMissionsSerializer(trend_mission, many=True)
        return Response(serializer.data, status=200)
    

class TrendMissionDetailView(GenericAPIView):
    # 트레드 미션 상세 조회
    def get(self, request, pk):

        # 트렌드 미션 존재 여부 확인
        if not TrendMission.objects.filter(pk=pk).exists():
            return Response("존재하지 않는 트렌드 미션입니다.", status=404)

        trend_mission = TrendMission.objects.get(pk=pk)
        serializer = TrendMissionsSerializer(trend_mission)

        # 트렌드 미션에 해당하는 유저의 트렌드 아이템 리스트 조회
        user_trend_item_list = UserTrendItem.objects.filter(trend_mission_id=pk)
        result = serializer.data
        result["trend_item_list"] = user_trend_item_list.values()
        return Response(result, status=200)
    

class CheckMissionCompleteView(GenericAPIView):
    def patch(self, request, pk):
        # 트렌드 미션 존재 여부 확인
        if not TrendMission.objects.filter(pk=pk).exists():
            return Response("존재하지 않는 트렌드 미션입니다.", status=404)

        trend_mission = TrendMission.objects.get(pk=pk)
        user_id = request.data["user_id"]
        user_id = User.objects.get(pk=user_id)
        
        # 해당하는 트렌드 미션 아이템 목록 찾기
        trend_item_list = UserTrendItem.objects.filter(trend_mission_id=pk, user_id=user_id)
        
        # 모든 미션 완수 여부 확인 (인증 여부 확인)
        for trend_item in trend_item_list:
            if trend_item.is_certificated == False:
                return Response("아직 모든 미션을 완료하지 않았습니다.", status=202)

        # 트렌드 미션 상태값 변경 -> True
        trend_mission.is_all_certificated = True
        serializer = TrendMissionsSerializer(trend_mission)
        serializer.updateComplete(trend_mission)

        # 스탬프 발급
        if Stamp.objects.filter(user_id=user_id, trend_mission_id=trend_mission).exists():
            return Response("이미 스탬프를 발급받았습니다.", status=404)
        
        stamp = Stamp.objects.create(
            user_id=user_id,
            trend_mission_id=trend_mission,
        )

        return Response(serializer.data, status=200)