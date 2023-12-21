from rest_framework import serializers
from .models import Trend, TrendItem
from trend_missions.models import UserTrendItem


class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = ["id", "name", "view_count", "created_at", "image"]


class TrendViewCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = ["view_count"]


class TrendItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendItem
        fields = ["id", "trend", "title", "content", "image"]


class TrendsUserTrendItemSerializer(serializers.ModelSerializer):
    trend_name = serializers.CharField(
        source="trend_mission.trend.name", read_only=True
    )

    class Meta:
        model = UserTrendItem
        fields = [
            "trend_name",
            "id",
            "user",
            "trend_mission",
            "updated_at",
            "image",
        ]
