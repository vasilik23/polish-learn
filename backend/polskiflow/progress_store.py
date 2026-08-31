"""RLS-aware persistence through the Supabase Data API."""

import json
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.conf import settings

from polskiflow.domain.progress import current_streak


@dataclass(frozen=True)
class DashboardProgress:
    display_name: str
    level: str
    streak_days: int
    completed_lesson_ids: frozenset[str]
    available: bool
    all_completed_lesson_ids: frozenset[str] = frozenset()
    active_days: int = 0
    weekly_active_days: int = 0
    weekly_completed_count: int = 0
    previous_week_active_days: int = 0
    previous_week_completed_count: int = 0
    monthly_active_days: int = 0
    monthly_completed_count: int = 0
    daily_goal_lessons: int = 4
    recent_daily_completion_counts: tuple[int, ...] = ()

    @property
    def completed_count(self) -> int:
        return len(self.completed_lesson_ids)

    @property
    def weekly_active_days_delta(self) -> int:
        return self.weekly_active_days - self.previous_week_active_days

    @property
    def weekly_completed_delta(self) -> int:
        return self.weekly_completed_count - self.previous_week_completed_count


def load_dashboard_progress(
    access_token: str | None,
    user_id: str,
    fallback_name: str,
) -> DashboardProgress:
    """Read the signed-in learner's profile and completion history via RLS."""

    if not _configured(access_token):
        return _empty_dashboard(fallback_name)

    profile = _get_rows(
        "profiles",
        {"select": "display_name,level,daily_goal_lessons", "id": f"eq.{user_id}", "limit": "1"},
        access_token,
    )
    completions = _get_rows(
        "lesson_completions",
        {
            "select": "lesson_id,plan_date",
            "user_id": f"eq.{user_id}",
            "order": "plan_date.desc",
            "limit": "1500",
        },
        access_token,
    )
    profile_row = profile[0] if profile else {}
    completion_rows = completions or []
    today = _utc_today()
    active_dates = []
    weekly_dates = set()
    weekly_lesson_ids = set()
    previous_week_dates = set()
    previous_week_lesson_ids = set()
    monthly_dates = set()
    monthly_lesson_ids = set()
    completed_today = set()
    completed_all_time = set()
    recent_lessons_by_date = {
        today - timedelta(days=offset): set() for offset in range(28)
    }
    for completion in completion_rows:
        try:
            plan_date = datetime.strptime(completion["plan_date"], "%Y-%m-%d").date()
        except (KeyError, TypeError, ValueError):
            continue
        active_dates.append(plan_date)
        lesson_id = completion.get("lesson_id")
        if lesson_id and plan_date in recent_lessons_by_date:
            recent_lessons_by_date[plan_date].add(lesson_id)
        if today - timedelta(days=29) <= plan_date <= today:
            monthly_dates.add(plan_date)
            if lesson_id:
                monthly_lesson_ids.add(lesson_id)
        if today - timedelta(days=6) <= plan_date <= today:
            weekly_dates.add(plan_date)
            if lesson_id:
                weekly_lesson_ids.add(lesson_id)
        elif today - timedelta(days=13) <= plan_date <= today - timedelta(days=7):
            previous_week_dates.add(plan_date)
            if lesson_id:
                previous_week_lesson_ids.add(lesson_id)
        if lesson_id:
            completed_all_time.add(lesson_id)
            if plan_date == today:
                completed_today.add(lesson_id)

    return DashboardProgress(
        display_name=profile_row.get("display_name") or fallback_name,
        level=profile_row.get("level") or "A1",
        streak_days=current_streak(active_dates, today),
        completed_lesson_ids=frozenset(completed_today),
        available=profile is not None and completions is not None,
        all_completed_lesson_ids=frozenset(completed_all_time),
        active_days=len(set(active_dates)),
        weekly_active_days=len(weekly_dates),
        weekly_completed_count=len(weekly_lesson_ids),
        previous_week_active_days=len(previous_week_dates),
        previous_week_completed_count=len(previous_week_lesson_ids),
        monthly_active_days=len(monthly_dates),
        monthly_completed_count=len(monthly_lesson_ids),
        daily_goal_lessons=profile_row.get("daily_goal_lessons") or 4,
        recent_daily_completion_counts=tuple(
            len(recent_lessons_by_date[today - timedelta(days=offset)])
            for offset in range(27, -1, -1)
        ),
    )


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

    if not _configured(access_token):
        return False
    query = urlencode({"on_conflict": "user_id,lesson_id,plan_date"})
    payload = {
        "user_id": user_id,
        "lesson_id": lesson_id,
        "plan_date": _utc_today().isoformat(),
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


def save_profile_settings(
    access_token: str | None,
    user_id: str,
    display_name: str,
    level: str,
    daily_goal_lessons: int = 4,
) -> bool:
    """Update the authenticated learner's existing profile through RLS."""

    if not _configured(access_token):
        return False
    request = Request(
        f"{settings.SUPABASE_URL.rstrip('/')}/rest/v1/profiles?"
        f"{urlencode({'id': f'eq.{user_id}'})}",
        data=json.dumps({"display_name": display_name, "level": level, "daily_goal_lessons": daily_goal_lessons}).encode(),
        method="PATCH",
        headers={
            "apikey": settings.SUPABASE_ANON_KEY,
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal",
        },
    )
    try:
        with urlopen(request, timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            return response.status in (200, 204)
    except (HTTPError, URLError, TimeoutError):
        return False


def _get_rows(table: str, query: dict[str, str], access_token: str) -> list[dict] | None:
    request = Request(
        f"{settings.SUPABASE_URL.rstrip('/')}/rest/v1/{table}?{urlencode(query)}",
        headers={
            "apikey": settings.SUPABASE_ANON_KEY,
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
        },
    )
    try:
        with urlopen(request, timeout=settings.SUPABASE_AUTH_TIMEOUT) as response:
            rows = json.load(response)
            return rows if isinstance(rows, list) else None
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
        return None


def _configured(access_token: str | None) -> bool:
    return bool(settings.SUPABASE_URL and settings.SUPABASE_ANON_KEY and access_token)


def _empty_dashboard(fallback_name: str) -> DashboardProgress:
    return DashboardProgress(fallback_name, "A1", 0, frozenset(), False)


def _utc_today():
    return datetime.now(timezone.utc).date()
