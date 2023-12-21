from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts import views

urlpatterns = [
    path("oauth/kakao/login/", views.KakaoLogin.as_view(), name="kakao_login"),
    path("oauth/kakao/callback/", views.KakaoCallback.as_view(), name="kakao_callback"),
    path("oauth/kakao/logout/", views.KakaoLogout.as_view(), name="kakao_logout"),
    path(
        "oauth/kakao/logout/callback/",
        views.KakaoLogoutCallback.as_view(),
        name="kakao_logout_callback",
    ),
    path("oauth/kakao/unlink/", KakaoUnlink.as_view(), name="kakao_unlink"),
    path("oauth/kakao/unlink/", views.KakaoUnlink.as_view(), name="kakao_unlink"),
    path("users/<int:pk>", views.UserProfileView.as_view(), name="user_detail"),
    path("users/<int:user_id>/following", FollowingView.as_view(), name="following"),
    path("users/<int:user_id>/followers", FollowerView.as_view(), name="followers"),
]
