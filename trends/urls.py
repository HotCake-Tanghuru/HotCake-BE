from django.urls import path
from . import views

urlpatterns = [
    path("", views.TrendView.as_view(), name="trends"),
    path("<int:trend_id>/", views.TrendDetailView.as_view(), name="trend_detail"),
    path("<int:trend_id>/likes/", views.TrendLikeView.as_view(), name="trend_like"),
    path(
        "<int:user_id>/likelist/",
        views.TrendLikeListView.as_view(),
        name="trend_like_list",
    ),
]
