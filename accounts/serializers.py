from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User, Like


class UserSerializer(serializers.Serializer):
    social_id = serializers.CharField(max_length=100, help_text="소셜사용자_아이디")
    social_type = serializers.CharField(max_length=20, help_text="소셜 타입")
    email = serializers.EmailField(max_length=100, help_text="이메일")
    nickname = serializers.CharField(max_length=200, help_text="닉네임")
    profile_img = serializers.ImageField(required=False, help_text="프로필 사진")
    bio = serializers.CharField(required=False, help_text="자기소개")

    class Meta:
        model = User
        fields = ["social_type", "social_id", "email", "nickname", "profile_img", "bio"]
        read_only_fields = ('social_id', 'social_type', 'created_at', 'last_login')

    def validate(self, data):
        user = authenticate(social_id=data.get("social_id"))
        if not user:
            raise serializers.ValidationError({"error": "계정이 이미 존재합니다"})
        return data

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "user", "trend", "trend_mission"]
