"""Owner-scoped mistake notebook through the Supabase Data API."""

import json
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.conf import settings


def load_mistakes(token, user_id):
    if not _configured(token):
        return []
    query = urlencode({"select": "lesson_id,question_position,last_wrong_at", "user_id": f"eq.{user_id}", "order": "last_wrong_at.desc", "limit": "200"})
    try:
        with urlopen(_request(f"learner_mistakes?{query}", token), timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            rows = json.load(response)
        return rows if isinstance(rows, list) else None
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, TypeError):
        return None


def set_mistake(token, user_id, lesson_id, position, wrong):
    if not _configured(token):
        return False
    if wrong:
        request = _request(
            "learner_mistakes?on_conflict=user_id,lesson_id,question_position", token, "POST",
            {"user_id": user_id, "lesson_id": lesson_id, "question_position": position, "last_wrong_at": datetime.now(timezone.utc).isoformat()},
            "resolution=merge-duplicates,return=minimal",
        )
    else:
        query = urlencode({"user_id": f"eq.{user_id}", "lesson_id": f"eq.{lesson_id}", "question_position": f"eq.{position}"})
        request = _request(f"learner_mistakes?{query}", token, "DELETE", prefer="return=minimal")
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
