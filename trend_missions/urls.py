from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.PostTrendMissionView.as_view(), name="post_trend_mission"),
]
