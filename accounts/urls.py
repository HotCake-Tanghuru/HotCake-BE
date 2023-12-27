from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts import views 

urlpatterns = [
    path("oauth/kakao/login/", views.KakaoLogin.as_view(), name="kakao_login"),
    path("oauth/kakao/callback/", views.KakaoCallback.as_view(), name="kakao_callback"),

    path("oauth/kakao/login/fe", views.KakaoLoginFE.as_view(), name="kakao_login_fe"),
    path('oauth/kakao/callback/fe', views.KakaoLoginFE.as_view(), name='kakao_callback_fe'),

    path("oauth/kakao/logout/", views.KakaoLogout.as_view(), name="kakao_logout"),
    path(
        "oauth/kakao/logout/callback/",
        views.KakaoLogoutCallback.as_view(),
        name="kakao_logout_callback",
    ),
    path("oauth/kakao/unlink/", views.KakaoUnlink.as_view(), name="kakao_unlink"),
    path("users/<int:pk>", views.UserProfileView.as_view(), name="user_detail"),
    path("users/<int:user_id>/following", views.FollowingView.as_view(), name="following"),
    path("users/<int:user_id>/followers", views.FollowerView.as_view(), name="followers"),
    path("users/search", views.UserSearch.as_view(), name="follow"),
    path("users/info", views.UserInfo.as_view(), name="user_info"),
    # path('kakao/login/finish/', views.kakaoLoginFinish.as_view(),
    #     name='kakao_login_todjango'),
]
