from rest_framework import serializers
from .models import TrendMission, Stamp


class PostTrendMissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendMission
        fields = ["user_id", "trend_id"]


class TrendMissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendMission
        fields = ["id", "user_id", "trend_id", "is_all_certificated", "view_count"]

    # is_all_certificated True로 변경
    def updateComplete(self, instance):
        instance.is_all_certificated = True
        instance.save()
        return instance
    
class StampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stamp
        fields = ["user_id", "trend_id"]
