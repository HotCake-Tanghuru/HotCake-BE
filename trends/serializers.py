from rest_framework import serializers
from .models import Trend, TrendItem


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
