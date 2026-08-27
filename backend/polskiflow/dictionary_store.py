"""RLS-aware personal dictionary persistence through the Supabase Data API."""

import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.conf import settings

from polskiflow.domain.sm2 import Sm2Result


def load_personal_words(access_token: str | None, user_id: str) -> list[dict] | None:
    if not _configured(access_token):
        return []
    query = urlencode(
        {
            "select": (
                "id,word,translation,context,source_text_id,created_at,"
                "ease_factor,interval_days,repetitions,next_review_date,"
                "last_reviewed_at"
            ),
            "user_id": f"eq.{user_id}",
            "order": "created_at.desc",
            "limit": "500",
        }
    )
    request = _request(f"personal_words?{query}", access_token)
    try:
        with urlopen(request, timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            rows = json.load(response)
            return rows if isinstance(rows, list) else None
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
        return None


def save_personal_word(
    access_token: str | None,
    user_id: str,
    word: str,
    translation: str,
    context: str,
    source_text_id: str,
) -> bool:
    if not _configured(access_token):
        return False
    query = urlencode({"on_conflict": "user_id,word"})
    payload = {
        "user_id": user_id,
        "word": word,
        "translation": translation,
        "context": context,
        "source_text_id": source_text_id,
    }
    request = _request(
        f"personal_words?{query}",
        access_token,
        method="POST",
        payload=payload,
        prefer="resolution=merge-duplicates,return=minimal",
    )
    return _send(request)


def delete_personal_word(
    access_token: str | None, user_id: str, word_id: str
) -> bool:
    if not _configured(access_token):
        return False
    query = urlencode({"id": f"eq.{word_id}", "user_id": f"eq.{user_id}"})
    request = _request(
        f"personal_words?{query}", access_token, method="DELETE", prefer="return=minimal"
    )
    return _send(request)


def save_personal_word_review(
    access_token: str | None,
    user_id: str,
    word_id: str,
    result: Sm2Result,
    reviewed_at: str,
) -> bool:
    """Persist an SM-2 result without allowing ownership to be changed."""

    if not _configured(access_token):
        return False
    query = urlencode({"id": f"eq.{word_id}", "user_id": f"eq.{user_id}"})
    payload = {
        "ease_factor": result.ease_factor,
        "interval_days": result.interval_days,
        "repetitions": result.repetitions,
        "next_review_date": result.next_review_date.isoformat(),
        "last_reviewed_at": reviewed_at,
    }
    request = _request(
        f"personal_words?{query}",
        access_token,
        method="PATCH",
        payload=payload,
        prefer="return=minimal",
    )
    return _send(request)


def _request(
    path: str,
    access_token: str,
    method: str = "GET",
    payload: dict | None = None,
    prefer: str | None = None,
) -> Request:
    headers = {
        "apikey": settings.SUPABASE_ANON_KEY,
        "Authorization": f"Bearer {access_token}",
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


def _send(request: Request) -> bool:
    try:
        with urlopen(request, timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            return response.status in (200, 201, 204)
    except (HTTPError, URLError, TimeoutError):
        return False


def _configured(access_token: str | None) -> bool:
    return bool(settings.SUPABASE_URL and settings.SUPABASE_ANON_KEY and access_token)
