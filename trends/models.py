from django.db import models


class Trend(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="트렌드 이름")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    view_count = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="media/image/trend/", verbose_name="트렌드 사진")

    def __str__(self):
        return self.name


class TrendItem(models.Model):
    id = models.AutoField(primary_key=True)
    trend = models.ManyToManyField(Trend, verbose_name="트렌드")
    title = models.CharField(max_length=100, verbose_name="트렌드 아이템 제목")
    content = models.CharField(max_length=300, verbose_name="트렌드 아이템 내용")
    image = models.ImageField(
        upload_to="media/image/trendItem/", verbose_name="트렌드 아이템 사진"
    )

    def __str__(self):
        return self.title
