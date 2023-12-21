from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User, Like, Follow


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
        read_only_fields = ("social_id", "social_type")

    def validate(self, data):
        user = authenticate(social_id=data.get("social_id"))
        if not user:
            raise serializers.ValidationError({"error": "계정이 이미 존재합니다"})
        return data

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, data):
        """토큰 유효 검증"""
        try:
            self.token = data["refresh_token"]
        except:
            raise serializers.ValidationError({"error": "Invalid Token"})

        return data

    def save(self, **kwargs):
        """토큰을 블랙리스트에 추가"""
        try:
            RefreshToken(self.token).blacklist()

        except TokenError as ex:
            raise exceptions.AuthenticationFailed(ex)

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "user", "trend", "trend_mission"]

class FollowSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source="to_user", read_only=True)
    class Meta:
        model = Follow
        fields = ["id", "from_user", "to_user", "user_info"]
    
    def create(self, validated_data):
        follow = Follow.objects.create(**validated_data)
        return follow