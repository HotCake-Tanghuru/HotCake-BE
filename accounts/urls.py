from django.urls import path
from accounts.views import (
    KakaoLogin,
    KakaoCallback,
    KakaoLogout,
    KakaoLogoutCallback,
    KakaoUnlink,
    FollowingView,
)

urlpatterns = [
    path("oauth/kakao/login/", KakaoLogin.as_view(), name="kakao_login"),
    path("oauth/kakao/callback/", KakaoCallback.as_view(), name="kakao_callback"),
    path("oauth/kakao/logout/", KakaoLogout.as_view(), name="kakao_logout"),
    path(
        "oauth/kakao/logout/callback/",
        KakaoLogoutCallback.as_view(),
        name="kakao_logout_callback",
    ),
    path("oauth/kakao/unlink/", KakaoUnlink.as_view(), name="kakao_unlink"),

    path("users/<int:user_id>/following", FollowingView.as_view(), name="following"),
    
]
