"""Supabase Auth client and request authentication for the Django app."""

from __future__ import annotations

import json
from dataclasses import dataclass
from functools import wraps
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from django.conf import settings
from django.http import JsonResponse

ACCESS_COOKIE = "polskiflow_access_token"
REFRESH_COOKIE = "polskiflow_refresh_token"
REFRESH_COOKIE_MAX_AGE = 60 * 60 * 24 * 30


@dataclass(frozen=True)
class SupabaseUser:
    id: str
    email: str | None


@dataclass(frozen=True)
class SupabaseSession:
    access_token: str
    refresh_token: str
    expires_in: int
    user: SupabaseUser


class SupabaseAuthError(Exception):
    """A safe, user-facing Supabase Auth failure."""


class SupabaseAuthMiddleware:
    """Resolve an optional Bearer token through Supabase Auth.

    Token verification stays with Supabase, so Django does not depend on the
    project's current JWT signing algorithm or copy a signing secret.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.supabase_user = None
        request.supabase_access_token = None
        authorization = request.headers.get("Authorization", "")
        scheme, _, token = authorization.partition(" ")
        bearer_token = token if scheme.lower() == "bearer" and token else None
        access_token = bearer_token or request.COOKIES.get(ACCESS_COOKIE)

        if access_token:
            request.supabase_user = authenticate_access_token(access_token)
            if request.supabase_user is not None:
                request.supabase_access_token = access_token

        refreshed_session = None
        clear_cookies = False
        if (
            request.supabase_user is None
            and bearer_token is None
            and request.COOKIES.get(REFRESH_COOKIE)
        ):
            try:
                refreshed_session = refresh_session(request.COOKIES[REFRESH_COOKIE])
            except SupabaseAuthError:
                clear_cookies = True
            else:
                request.supabase_user = refreshed_session.user
                request.supabase_access_token = refreshed_session.access_token

        response = self.get_response(request)
        if refreshed_session is not None:
            set_auth_cookies(response, refreshed_session)
        elif clear_cookies:
            clear_auth_cookies(response)
        return response


def authenticate_access_token(token: str) -> SupabaseUser | None:
    if not settings.SUPABASE_URL or not settings.SUPABASE_ANON_KEY:
        return None

    request = Request(
        f"{settings.SUPABASE_URL.rstrip('/')}/auth/v1/user",
        headers={
            "apikey": settings.SUPABASE_ANON_KEY,
            "Authorization": f"Bearer {token}",
        },
    )
    try:
        with urlopen(request, timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            payload = json.load(response)
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
        return None

    user_id = payload.get("id")
    if not isinstance(user_id, str):
        return None
    email = payload.get("email")
    return SupabaseUser(id=user_id, email=email if isinstance(email, str) else None)


def sign_in(email: str, password: str) -> SupabaseSession:
    payload = _auth_request(
        "/auth/v1/token?grant_type=password",
        {"email": email, "password": password},
    )
    return _parse_session(payload)


def sign_up(email: str, password: str) -> SupabaseSession | None:
    payload = _auth_request("/auth/v1/signup", {"email": email, "password": password})
    if not payload.get("access_token"):
        return None
    return _parse_session(payload)


def refresh_session(refresh_token: str) -> SupabaseSession:
    payload = _auth_request(
        "/auth/v1/token?grant_type=refresh_token",
        {"refresh_token": refresh_token},
    )
    return _parse_session(payload)


def sign_out(access_token: str) -> None:
    _auth_request("/auth/v1/logout", {}, access_token=access_token)


def set_auth_cookies(response, session: SupabaseSession) -> None:
    cookie_options = {
        "httponly": True,
        "secure": settings.AUTH_COOKIE_SECURE,
        "samesite": "Lax",
        "path": "/",
    }
    response.set_cookie(
        ACCESS_COOKIE,
        session.access_token,
        max_age=session.expires_in,
        **cookie_options,
    )
    response.set_cookie(
        REFRESH_COOKIE,
        session.refresh_token,
        max_age=REFRESH_COOKIE_MAX_AGE,
        **cookie_options,
    )


def clear_auth_cookies(response) -> None:
    response.delete_cookie(ACCESS_COOKIE, path="/", samesite="Lax")
    response.delete_cookie(REFRESH_COOKIE, path="/", samesite="Lax")


def _auth_request(
    path: str, payload: dict[str, str], access_token: str | None = None
) -> dict:
    if not settings.SUPABASE_URL or not settings.SUPABASE_ANON_KEY:
        raise SupabaseAuthError("Supabase не настроен")

    body = json.dumps(payload).encode()
    headers = {
        "apikey": settings.SUPABASE_ANON_KEY,
        "Content-Type": "application/json",
    }
    if access_token:
        headers["Authorization"] = f"Bearer {access_token}"
    request = Request(
        f"{settings.SUPABASE_URL.rstrip('/')}{path}",
        data=body,
        headers=headers,
        method="POST",
    )
    try:
        with urlopen(request, timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            if response.status == 204:
                return {}
            result = json.load(response)
    except HTTPError as error:
        raise SupabaseAuthError(_http_error_message(error)) from error
    except (URLError, TimeoutError, json.JSONDecodeError) as error:
        raise SupabaseAuthError("Сервис авторизации временно недоступен") from error
    if not isinstance(result, dict):
        raise SupabaseAuthError("Некорректный ответ сервиса авторизации")
    return result


def _http_error_message(error: HTTPError) -> str:
    try:
        payload = json.load(error)
    except (json.JSONDecodeError, AttributeError):
        return "Не удалось выполнить авторизацию"
    message = payload.get("msg") or payload.get("message") or payload.get("error_description")
    return message if isinstance(message, str) else "Не удалось выполнить авторизацию"


def _parse_session(payload: dict) -> SupabaseSession:
    access_token = payload.get("access_token")
    refresh_token = payload.get("refresh_token")
    expires_in = payload.get("expires_in", 3600)
    user_payload = payload.get("user")
    if not isinstance(access_token, str) or not isinstance(refresh_token, str):
        raise SupabaseAuthError("Сессия не была создана")
    if not isinstance(user_payload, dict) or not isinstance(user_payload.get("id"), str):
        raise SupabaseAuthError("Ответ авторизации не содержит пользователя")
    email = user_payload.get("email")
    return SupabaseSession(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=expires_in if isinstance(expires_in, int) else 3600,
        user=SupabaseUser(
            id=user_payload["id"],
            email=email if isinstance(email, str) else None,
        ),
    )


def require_supabase_user(view):
    @wraps(view)
    def protected(request, *args, **kwargs):
        if request.supabase_user is None:
            return JsonResponse({"detail": "Authentication required"}, status=401)
        return view(request, *args, **kwargs)

    return protected
