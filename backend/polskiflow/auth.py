"""Supabase access-token authentication for the transitional Django app."""

from __future__ import annotations

import json
from dataclasses import dataclass
from functools import wraps
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from django.conf import settings
from django.http import JsonResponse


@dataclass(frozen=True)
class SupabaseUser:
    id: str
    email: str | None


class SupabaseAuthMiddleware:
    """Resolve an optional Bearer token through Supabase Auth.

    Token verification stays with Supabase, so Django does not depend on the
    project's current JWT signing algorithm or copy a signing secret.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.supabase_user = None
        authorization = request.headers.get("Authorization", "")
        scheme, _, token = authorization.partition(" ")
        if scheme.lower() == "bearer" and token:
            request.supabase_user = authenticate_access_token(token)
        return self.get_response(request)


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


def require_supabase_user(view):
    @wraps(view)
    def protected(request, *args, **kwargs):
        if request.supabase_user is None:
            return JsonResponse({"detail": "Authentication required"}, status=401)
        return view(request, *args, **kwargs)

    return protected
