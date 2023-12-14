from rest_framework import serializers
from .models import TrendMission

class PostTrendMissionsSerializer(serializers.ModelSerializer):
  class Meta:
    model = TrendMission
    fields = ['user_id', 'trend_id']

class TrendMissionsSerializer(serializers.ModelSerializer):
  class Meta:
    model = TrendMission
    fields = ['id', 'user_id', 'trend_id', 'is_all_certificated', 'view_count']
  