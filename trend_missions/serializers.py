from rest_framework import serializers
from .models import TrendMission, UserTrendItem

class PostTrendMissionsSerializer(serializers.ModelSerializer):
  class Meta:
    model = TrendMission
    fields = ['user_id', 'trend_id']

class TrendMissionsSerializer(serializers.ModelSerializer):
  class Meta:
    model = TrendMission
    fields = ['id', 'user_id', 'trend_id', 'is_all_certificated', 'view_count']

class UserTrendItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserTrendItem
    fields = ['id', 'user_id', 'trend_mission_id', 'trend_item_id', 'updated_at', 'image', 'is_certificated', 'content']

class UserTrendItemUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserTrendItem
    fields = ['user_id', 'image', 'content']