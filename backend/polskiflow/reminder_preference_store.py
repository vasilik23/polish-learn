"""Owner-scoped reminder preferences through the Supabase Data API."""

import json
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.conf import settings


DEFAULT_REMINDER_PREFERENCES = {
    "daily_reminder_enabled": False,
    "reminder_time": "19:00",
    "timezone": "Europe/Warsaw",
}


def load_reminder_preferences(access_token: str | None, user_id: str) -> dict | None:
    """Return safe defaults when no row exists, and None on Data API failure."""
    if not _configured(access_token):
        return DEFAULT_REMINDER_PREFERENCES.copy()
    query = urlencode(
        {
            "select": "daily_reminder_enabled,reminder_time,timezone",
            "user_id": f"eq.{user_id}",
            "limit": "1",
        }
    )
    try:
        with urlopen(
            _request(f"reminder_preferences?{query}", access_token),
            timeout=settings.SUPABASE_AUTH_TIMEOUT,
        ) as response:
            rows = json.load(response)
        if not rows:
            return DEFAULT_REMINDER_PREFERENCES.copy()
        row = rows[0]
        return {
            "daily_reminder_enabled": row.get("daily_reminder_enabled") is True,
            "reminder_time": str(row.get("reminder_time") or "19:00")[:5],
            "timezone": row.get("timezone") or "Europe/Warsaw",
        }
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, TypeError):
        return None


def save_reminder_preferences(
    access_token: str | None,
    user_id: str,
    daily_reminder_enabled: bool,
    reminder_time: str,
    timezone_name: str,
) -> bool:
    if not _configured(access_token):
        return False
    request = _request(
        "reminder_preferences?on_conflict=user_id",
        access_token,
        "POST",
        {
            "user_id": user_id,
            "daily_reminder_enabled": daily_reminder_enabled,
            "reminder_time": reminder_time,
            "timezone": timezone_name,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        },
        "resolution=merge-duplicates,return=minimal",
    )
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
