from django.urls import path
from . import views

urlpatterns = [
    path("create", views.PostTrendMissionView.as_view(), name="post_trend_mission"),
    path("<int:pk>", views.TrendMissionListView.as_view(), name="trend_mission_list"),
    path("about/<int:pk>", views.TrendMissionDetailView.as_view(), name="trend_mission_detail"),
    path("mission-item/<int:pk>/edit", views.TrendMissionItemUpdateView.as_view(), name="trend_mission_item_update"),
    path("<int:pk>/complete", views.CheckMissionCompleteView.as_view(), name="trend_mission_complete"),
    path("users/<int:user_id>/stamp", views.StampListView.as_view(), name="stamp_list"),
]
