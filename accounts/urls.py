from django.urls import path
from accounts.views import KakaoLogin, KakaoCallback, KakaoLogin

urlpatterns = [
    path("oauth/kakao/login/", KakaoLogin.as_view(), name="kakao_login"),
    path("oauth/kakao/callback/", KakaoCallback.as_view(), name="kakao_callback"),
]
