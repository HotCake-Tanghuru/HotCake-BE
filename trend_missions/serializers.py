from rest_framework import serializers
from .models import TrendMission, UserTrendItem


class PostTrendMissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendMission
        fields = ["user", "trend"]


class TrendMissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendMission
        fields = ["id", "user", "trend", "is_all_certificated", "view_count"]


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
