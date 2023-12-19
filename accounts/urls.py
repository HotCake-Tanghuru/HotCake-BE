from django.urls import path
from accounts.views import KakaoLogin, KakaoCallback, KakaoLogout, KakaoLogoutCallback

urlpatterns = [
    path("oauth/kakao/login/", KakaoLogin.as_view(), name="kakao_login"),
    path("oauth/kakao/callback/", KakaoCallback.as_view(), name="kakao_callback"),
    path("oauth/kakao/logout/", KakaoLogout.as_view(), name="kakao_logout"),
    path(
        "oauth/kakao/logout/callback/",
        KakaoLogoutCallback.as_view(),
        name="kakao_logout_callback",
    ),
]
