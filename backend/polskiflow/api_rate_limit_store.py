"""Distributed mutation quotas through an authenticated Supabase RPC."""

import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from django.conf import settings


def consume_distributed_api_mutation(access_token: str | None, action: str) -> tuple[bool, int] | None:
    if not (settings.SUPABASE_URL and settings.SUPABASE_ANON_KEY and access_token):
        return None
    request = Request(
        f"{settings.SUPABASE_URL.rstrip('/')}/rest/v1/rpc/consume_api_mutation",
        data=json.dumps({"p_action": action}).encode(), method="POST",
        headers={
            "apikey": settings.SUPABASE_ANON_KEY,
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urlopen(request, timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            rows = json.load(response)
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
        return None
    if not isinstance(rows, list) or len(rows) != 1 or not isinstance(rows[0], dict):
        return None
    allowed, retry_after = rows[0].get("allowed"), rows[0].get("retry_after")
    if not isinstance(allowed, bool) or isinstance(retry_after, bool) or not isinstance(retry_after, int):
        return None
    return allowed, max(1, retry_after)
