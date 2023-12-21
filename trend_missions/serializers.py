from rest_framework import serializers
from .models import TrendMission, UserTrendItem, Stamp, Comment
from accounts.models import User

class PostTrendMissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendMission
        fields = ["trend"]
    


class TrendMissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendMission
        fields = ["id", "user", "trend", "is_all_certificated", "view_count"]

    # is_all_certificated True로 변경
    def updateComplete(self, instance):
        instance.is_all_certificated = True
        instance.save()
        return instance

    # view_count 1 증가
    def updateViewCount(self, instance):
        instance.view_count += 1
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
        fields = ["image", "content"]


class StampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stamp
        fields = ["user", "trend_mission", "created_at"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "user",
            "trend_mission",
            "content",
            "created_at",
            "updated_at",
            "parent_comment",
        ]
