from django.urls import path
from . import views

urlpatterns = [
    path("create", views.PostTrendMissionView.as_view(), name="post_trend_mission"),
    path("<int:pk>", views.TrendMissionListView.as_view(), name="trend_mission_list"),
    path("about/<int:pk>", views.TrendMissionDetailView.as_view(), name="trend_mission_detail"),
]
