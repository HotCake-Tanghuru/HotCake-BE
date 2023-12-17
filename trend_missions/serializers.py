from rest_framework import serializers
from .models import TrendMission, UserTrendItem, Stamp



class PostTrendMissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendMission
        fields = ["user", "trend"]



class TrendMissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendMission
        fields = ["id", "user", "trend", "is_all_certificated", "view_count"]

    # is_all_certificated True로 변경
    def updateComplete(self, instance):
        instance.is_all_certificated = True
        instance.save()
        return instance


class UserTrendItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTrendItem
        fields = [
            "id",
            "user",
            "trend_mission",
            "trend_item",
            "updated_at",
            "image",
            "is_certificated",
            "content",
        ]


class UserTrendItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTrendItem
        fields = ["user", "image", "content"]


    
class StampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stamp
        fields = ["user", "trend_mission", "created_at"]

