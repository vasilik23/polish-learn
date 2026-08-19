"""Minimal settings for the incremental Django migration."""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "unsafe-local-development-key")
DEBUG = os.environ.get("DJANGO_DEBUG", "true").lower() == "true"
ALLOWED_HOSTS = [host for host in os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",") if host]

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "polskiflow.learning",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "polskiflow.auth.SupabaseAuthMiddleware",
]
ROOT_URLCONF = "polskiflow.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": []},
    }
]
WSGI_APPLICATION = "polskiflow.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = os.environ.get("APP_TIME_ZONE", "Europe/Warsaw")
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY", "")
SUPABASE_AUTH_TIMEOUT = float(os.environ.get("SUPABASE_AUTH_TIMEOUT", "5"))
AUTH_COOKIE_SECURE = os.environ.get("AUTH_COOKIE_SECURE", str(not DEBUG)).lower() == "true"
CSRF_COOKIE_SECURE = AUTH_COOKIE_SECURE
SECURE_SSL_REDIRECT = os.environ.get(
    "DJANGO_SECURE_SSL_REDIRECT", str(not DEBUG)
).lower() == "true"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_HSTS_SECONDS = int(os.environ.get("DJANGO_SECURE_HSTS_SECONDS", "0"))
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", "false"
).lower() == "true"
SECURE_HSTS_PRELOAD = os.environ.get(
    "DJANGO_SECURE_HSTS_PRELOAD", "false"
).lower() == "true"
X_FRAME_OPTIONS = "DENY"
