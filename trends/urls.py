from django.urls import path
from . import views

urlpatterns = [
    path("", views.TrendView.as_view(), name="trends"),
    path("<int:trend_id>/", views.TrendDetailView.as_view(), name="trend_detail"),
]