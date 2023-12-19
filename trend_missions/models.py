from django.db import models
from trends.models import Trend, TrendItem
from accounts.models import User


class TrendMission(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        verbose_name="사용자",
        on_delete=models.CASCADE,
    )
    trend = models.ForeignKey(Trend, verbose_name="트렌드", on_delete=models.PROTECT)
    is_all_certificated = models.BooleanField(verbose_name="인증 여부", default=False)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.nickname + "의 " + self.trend.name + "미션"


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        verbose_name="사용자",
        on_delete=models.CASCADE,
    )
    trend_mission = models.ForeignKey(
        TrendMission,
        verbose_name="트렌드 미션 아이디",
        on_delete=models.CASCADE,
    )
    content = models.CharField(max_length=300, verbose_name="댓글 내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.user.nickname + "의 " + self.trend_mission.trend.name + "댓글" + str(self.id)


class UserTrendItem(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        verbose_name="사용자",
        on_delete=models.CASCADE,
    )
    trend_mission = models.ForeignKey(
        TrendMission,
        verbose_name="트렌드 미션 아이디",
        on_delete=models.CASCADE,
    )
    trend_item = models.ForeignKey(
        TrendItem,
        verbose_name="트렌드 아이템 아이디",
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="인증날짜")
    image = models.ImageField(
        upload_to="media/image/userTrendItem/", verbose_name="트렌드 아이템 인증 사진"
    )
    is_certificated = models.BooleanField(verbose_name="인증 여부", default=False)
    content = models.CharField(max_length=300, verbose_name="트렌드 아이템 인증 내용")

    def __str__(self):
        return (
            self.user.nickname
            + "의 "
            + self.trend_mission.trend.name
            + " 트렌드 미션의 "
            + self.trend_item.title
        )


class Stamp(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        verbose_name="스탬프 소유자",
        on_delete=models.CASCADE,
    )
    trend_mission = models.ForeignKey(
        TrendMission,
        verbose_name="트렌드 미션 아이디",
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="스탬프 발급일")

    def __str__(self):
        return self.user.nickname + "의 " + self.trend_mission.trend.name + "스탬프"
