from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from trends.models import Trend


class UserManager(BaseUserManager):
    def create_user(
        self,
        social_type,
        social_id,
        email,
        nickname,
        profile_img=None,
        bio=None,
        password=None,
    ):
        if not email:
            raise ValueError("이메일은 필수입니다.")

        user = self.model(
            social_type=social_type,
            social_id=social_id,
            email=self.normalize_email(email),
            nickname=nickname,
            profile_img=profile_img,
            bio=bio,
        )

        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if not password:
            raise ValueError("슈퍼유저 생성을 위해서는 비밀번호가 필수입니다.")

        user = self.create_user(
            social_type=None,
            social_id=None,
            email=email,
            nickname=email.split("@")[0],
            profile_img=None,
            bio=None,
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    social_type = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="소셜 타입"
    )
    social_id = models.CharField(
        max_length=100, unique=True, blank=True, null=True, verbose_name="소셜사용자아이디"
    )
    email = models.EmailField(max_length=100, unique=True, verbose_name="이메일")
    nickname = models.CharField(max_length=200, verbose_name="닉네임")
    profile_img = models.ImageField(
        upload_to="image/profile/", blank=True, verbose_name="프로필 사진"
    )
    bio = models.TextField(blank=True, null=True, verbose_name="자기소개")
    password = models.CharField(max_length=100, blank=True)
    username = None
    first_name = None
    last_name = None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.nickname}({self.email})"


class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    from_user = models.ForeignKey(
        User,
        verbose_name="팔로우 하는 사용자",
        related_name="from_user",
        on_delete=models.CASCADE,
    )
    to_user = models.ForeignKey(
        User,
        verbose_name="팔로우 대상 사용자",
        related_name="to_user",
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name="사용자 아이디", on_delete=models.CASCADE)
    trend = models.ForeignKey(
        Trend,
        verbose_name="트렌드 아이디",
        related_name="trend",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    # 순환 참조 방지를 위해 아래와 같이 import
    from trend_missions.models import TrendMission

    trend_mission = models.ForeignKey(
        TrendMission,
        verbose_name="트렌드 미션 아이디",
        related_name="trend_mission",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
