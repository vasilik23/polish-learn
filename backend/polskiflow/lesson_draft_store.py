"""Owner-scoped cross-device lesson draft persistence."""

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.conf import settings


@dataclass(frozen=True)
class LessonDraftLoadResult:
    available: bool
    draft: dict | None = None


def load_lesson_draft(access_token, user_id, lesson_id):
    if not _configured(access_token): return None
    query = urlencode({"select": "lesson_kind,step_index,score", "user_id": f"eq.{user_id}", "lesson_id": f"eq.{lesson_id}", "limit": "1"})
    request = _request(f"lesson_drafts?{query}", access_token)
    try:
        with urlopen(request, timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            rows = json.load(response)
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError): return None
    return rows[0] if isinstance(rows, list) and rows else None


def load_latest_lesson_draft(access_token, user_id):
    """Return the learner's most recently updated unfinished lesson."""
    return load_latest_lesson_draft_result(access_token, user_id).draft


def load_latest_lesson_draft_result(access_token, user_id):
    """Distinguish an empty draft list from an unavailable Data API."""
    if not _configured(access_token): return LessonDraftLoadResult(False)
    query = urlencode({"select": "lesson_id,lesson_kind,step_index,score,updated_at", "user_id": f"eq.{user_id}", "order": "updated_at.desc", "limit": "1"})
    request = _request(f"lesson_drafts?{query}", access_token)
    try:
        with urlopen(request, timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            rows = json.load(response)
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
        return LessonDraftLoadResult(False)
    if not isinstance(rows, list):
        return LessonDraftLoadResult(False)
    return LessonDraftLoadResult(True, rows[0] if rows else None)


def save_lesson_draft(access_token, user_id, lesson_id, lesson_kind, step_index, score):
    if not _configured(access_token): return False
    query = urlencode({"on_conflict": "user_id,lesson_id"})
    payload = {"user_id": user_id, "lesson_id": lesson_id, "lesson_kind": lesson_kind, "step_index": step_index, "score": score, "updated_at": datetime.now(timezone.utc).isoformat()}
    request = _request(f"lesson_drafts?{query}", access_token, "POST", payload, "resolution=merge-duplicates,return=minimal")
    try:
        with urlopen(request, timeout=settings.SUPABASE_AUTH_TIMEOUT) as response: return response.status in (200, 201, 204)
    except (HTTPError, URLError, TimeoutError): return False


def delete_lesson_draft(access_token, user_id, lesson_id):
    if not _configured(access_token): return False
    query = urlencode({"user_id": f"eq.{user_id}", "lesson_id": f"eq.{lesson_id}"})
    request = _request(f"lesson_drafts?{query}", access_token, "DELETE", prefer="return=minimal")
    try:
        with urlopen(request, timeout=settings.SUPABASE_AUTH_TIMEOUT) as response: return response.status in (200, 204)
    except (HTTPError, URLError, TimeoutError): return False


def _request(path, token, method="GET", payload=None, prefer=None):
    headers = {"apikey": settings.SUPABASE_ANON_KEY, "Authorization": f"Bearer {token}", "Accept": "application/json"}
    if payload is not None: headers["Content-Type"] = "application/json"
    if prefer: headers["Prefer"] = prefer
    return Request(f"{settings.SUPABASE_URL.rstrip('/')}/rest/v1/{path}", data=json.dumps(payload).encode() if payload is not None else None, method=method, headers=headers)


def _configured(token): return bool(settings.SUPABASE_URL and settings.SUPABASE_ANON_KEY and token)
