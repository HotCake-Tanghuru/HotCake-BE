from datetime import timedelta
import environ, os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(env_file=BASE_DIR / ".env")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# DATABASES Related
DATABASES_ENGINE=env("DATABASES_ENGINE")
DATABASES_NAME=env("DATABASES_NAME")
DATABASES_USER=env("DATABASES_USER")
DATABASES_PASSWORD=env("DATABASES_PASSWORD")
DATABASES_HOST=env("DATABASES_HOST")
DATABASES_PORT=env("DATABASES_PORT")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # django-rest-framework
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    # swagger
    'drf_spectacular',
    # apps
    "accounts",
    "trends",
    "trend_missions",

    # cors
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware", # cors
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "hotcake.urls"

AUTH_USER_MODEL = "accounts.User"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [  # 기본 Permission 설정
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (  # Authenticationt 설정
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'AUTHENTICATION_SCHEME_NAMES': {
        'rest_framework_simplejwt.authentication.JWTAuthentication': 'bearer',
    },
    # 기타 설정...
    'TITLE': '핫 케이크 API 테스트 페이지',           
    'DESCRIPTION': 'oauth/kakao/login 페이지에서 로그인 후, access_token을 오른쪽에 있는 Authorize 버튼에 입력하면 테스트 가능합니다.',     
    'VERSION': '1.0.0',   
    # 이미지 파일 업로드
    'COMPONENT_SPLIT_REQUEST': True 
}

REST_USE_JWT = True

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=2),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    "BLACKLIST_AFTER_ROTATION": True,
}

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "hotcake.wsgi.application"


# Database
# postgresql 연결

DATABASES = {
    'default': {
    'ENGINE': DATABASES_ENGINE,
    'NAME': DATABASES_NAME,
    'USER': DATABASES_USER,
    'PASSWORD': DATABASES_PASSWORD,
    'HOST': DATABASES_HOST,
    'PORT': DATABASES_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

#CORS_ORIGIN_ALLOW_ALL = True
#SECURE_CROSS_ORIGIN_OPENER_POLICY = None

CORS_ORIGIN_WHITELIST = (
        "http://127.0.0.1:5500",
        "http://127.0.0.1:8000",
        "http://team-hotcake.s3-website.ap-northeast-2.amazonaws.com",
)
CORS_ALLOW_CREDENTIALS = True