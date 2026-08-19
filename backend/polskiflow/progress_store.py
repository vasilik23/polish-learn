"""RLS-aware persistence through the Supabase Data API."""

import json
from datetime import date
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.conf import settings


def save_lesson_completion(
    access_token: str | None,
    user_id: str,
    lesson_id: str,
    cards_total: int,
    cards_known: int,
) -> bool:
    """Upsert today's completion as the authenticated user.

    Local development without Supabase remains usable; in a configured
    environment, a rejected or unavailable write is reported to the UI.
    """

    if not settings.SUPABASE_URL or not settings.SUPABASE_ANON_KEY or not access_token:
        return False
    query = urlencode({"on_conflict": "user_id,lesson_id,plan_date"})
    payload = {
        "user_id": user_id,
        "lesson_id": lesson_id,
        "plan_date": date.today().isoformat(),
        "cards_total": cards_total,
        "cards_known": cards_known,
    }
    request = Request(
        f"{settings.SUPABASE_URL.rstrip('/')}/rest/v1/lesson_completions?{query}",
        data=json.dumps(payload).encode(),
        method="POST",
        headers={
            "apikey": settings.SUPABASE_ANON_KEY,
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Prefer": "resolution=merge-duplicates,return=minimal",
        },
    )
    try:
        with urlopen(request, timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            return response.status in (200, 201, 204)
    except (HTTPError, URLError, TimeoutError):
        return False
