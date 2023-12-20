from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User, Follow, Like


class UserSerializer(serializers.ModelSerializer):
    profile_img = serializers.ImageField(use_url=True)

    class Meta:
        model = User
        fields = ["social_type", "social_id", "email", "nickname", "profile_img"]
        read_only_fields = ("social_id", "social_type")

    def validate(self, data):
        user = authenticate(social_id=data.get("social_id"))
        if not user:
            raise serializers.ValidationError({"error": "소셜 계정이 이미 존재합니다"})
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


class UserProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "nickname",
            "profile_img",
            "bio",
            "followers_count",
            "following_count",
        ]
        read_only_fields = ["followers_count", "following_count"]

    def get_followers_count(self, obj):
        followers = Follow.objects.filter(to_user=obj)
        return followers.count()

    def get_following_count(self, obj):
        following = Follow.objects.filter(from_user=obj)
        return following.count()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "user", "trend", "trend_mission"]
