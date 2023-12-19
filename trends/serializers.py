from rest_framework import serializers
from .models import Trend


class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = ["id", "name", "view_count", "created_at", "image"]


class TrendItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = ["id", "trend", "title", "content", "image"]
