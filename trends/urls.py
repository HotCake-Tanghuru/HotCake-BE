from django.urls import path
from . import views

urlpatterns = [
    path("", views.TrendView.as_view(), name="trends"),
]
