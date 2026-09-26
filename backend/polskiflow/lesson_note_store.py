"""Owner-scoped lesson notes through the Supabase Data API."""

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.conf import settings


@dataclass(frozen=True)
class LessonNote:
    available: bool
    body: str = ""
    updated_at: str | None = None


def load_lesson_note(token, user_id, lesson_id):
    if not _configured(token):
        return LessonNote(False)
    query = urlencode({"select": "body,updated_at", "user_id": f"eq.{user_id}", "lesson_id": f"eq.{lesson_id}", "limit": "1"})
    try:
        with urlopen(_request(f"lesson_notes?{query}", token), timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            rows = json.load(response)
        if not isinstance(rows, list):
            return LessonNote(False)
        if not rows:
            return LessonNote(True)
        row = rows[0]
        if not isinstance(row, dict) or not isinstance(row.get("body"), str):
            return LessonNote(False)
        return LessonNote(True, row["body"], row.get("updated_at"))
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, TypeError):
        return LessonNote(False)


def load_lesson_notes(token, user_id):
    """Load the owner's note index, newest first, without exposing other rows."""
    if not _configured(token):
        return None
    query = urlencode({"select": "lesson_id,body,updated_at", "user_id": f"eq.{user_id}", "order": "updated_at.desc", "limit": "200"})
    try:
        with urlopen(_request(f"lesson_notes?{query}", token), timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            rows = json.load(response)
        if not isinstance(rows, list):
            return None
        return [row for row in rows if isinstance(row, dict) and isinstance(row.get("lesson_id"), str) and isinstance(row.get("body"), str)]
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, TypeError):
        return None


def save_lesson_note(token, user_id, lesson_id, body):
    if not _configured(token):
        return False
    body = body.strip()
    if not body:
        query = urlencode({"user_id": f"eq.{user_id}", "lesson_id": f"eq.{lesson_id}"})
        request = _request(f"lesson_notes?{query}", token, "DELETE", prefer="return=minimal")
    else:
        request = _request(
            "lesson_notes?on_conflict=user_id,lesson_id", token, "POST",
            {"user_id": user_id, "lesson_id": lesson_id, "body": body, "updated_at": datetime.now(timezone.utc).isoformat()},
            "resolution=merge-duplicates,return=minimal",
        )
    try:
        with urlopen(request, timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            return response.status in (200, 201, 204)
    except (HTTPError, URLError, TimeoutError):
        return False


def _request(path, token, method="GET", payload=None, prefer=None):
    headers = {"apikey": settings.SUPABASE_ANON_KEY, "Authorization": f"Bearer {token}", "Accept": "application/json"}
    if payload is not None:
        headers["Content-Type"] = "application/json"
    if prefer:
        headers["Prefer"] = prefer
    return Request(f"{settings.SUPABASE_URL.rstrip('/')}/rest/v1/{path}", data=json.dumps(payload).encode() if payload is not None else None, method=method, headers=headers)


def _configured(token):
    return bool(settings.SUPABASE_URL and settings.SUPABASE_ANON_KEY and token)
