"""Owner-scoped saved lessons through the Supabase Data API."""

import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.conf import settings


def load_lesson_bookmarks(access_token: str | None, user_id: str) -> set[str] | None:
    if not _configured(access_token):
        return set()
    query = urlencode({"select": "lesson_id", "user_id": f"eq.{user_id}", "limit": "1000"})
    try:
        with urlopen(_request(f"lesson_bookmarks?{query}", access_token), timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            rows = json.load(response)
        return {row["lesson_id"] for row in rows if isinstance(row, dict) and row.get("lesson_id")}
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, TypeError):
        return None


def set_lesson_bookmark(access_token: str | None, user_id: str, lesson_id: str, saved: bool) -> bool:
    if not _configured(access_token):
        return False
    if saved:
        request = _request(
            "lesson_bookmarks",
            access_token,
            "POST",
            {"user_id": user_id, "lesson_id": lesson_id},
            "resolution=ignore-duplicates,return=minimal",
        )
    else:
        query = urlencode({"user_id": f"eq.{user_id}", "lesson_id": f"eq.{lesson_id}"})
        request = _request(f"lesson_bookmarks?{query}", access_token, "DELETE", prefer="return=minimal")
    try:
        with urlopen(request, timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            return response.status in (200, 201, 204)
    except (HTTPError, URLError, TimeoutError):
        return False


def _request(path, token, method="GET", payload=None, prefer=None):
    headers = {
        "apikey": settings.SUPABASE_ANON_KEY,
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    if payload is not None:
        headers["Content-Type"] = "application/json"
    if prefer:
        headers["Prefer"] = prefer
    return Request(
        f"{settings.SUPABASE_URL.rstrip('/')}/rest/v1/{path}",
        data=json.dumps(payload).encode() if payload is not None else None,
        method=method,
        headers=headers,
    )


def _configured(token):
    return bool(settings.SUPABASE_URL and settings.SUPABASE_ANON_KEY and token)
