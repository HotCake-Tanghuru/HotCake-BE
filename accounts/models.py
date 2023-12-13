from django.db import models
from django.contrib.auth.models import AbstractUser
from trends.models import Trend


# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=200, verbose_name="닉네임")
    name = models.CharField(max_length=100, verbose_name="이름")
    email = models.EmailField(verbose_name="이메일")
    profile_img = models.ImageField(
        upload_to="media/image/profile/", blank=True, null=True, verbose_name="프로필 사진"
    )
    gender = models.CharField(max_length=10, verbose_name="성별")
    age_range = models.CharField(max_length=20, verbose_name="연령대")
    bio = models.TextField(blank=True, null=True, verbose_name="자기소개")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")


class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    from_user_id = models.ForeignKey(
        User,
        verbose_name="팔로우 하는 사용자",
        related_name="from_user",
        on_delete=models.CASCADE,
    )
    to_user_id = models.ForeignKey(
        User,
        verbose_name="팔로우 대상 사용자",
        related_name="to_user",
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, verbose_name="사용자 아이디", on_delete=models.CASCADE)
    trend_id = models.ForeignKey(
        Trend, verbose_name="트렌드 아이디",
        related_name="trend",
        on_delete=models.CASCADE
    )
    trend_mission_id = models.ForeignKey(
        Trend,
        verbose_name="트렌드 미션 아이디",
        related_name="trend_mission",
        on_delete=models.CASCADE,
    )
