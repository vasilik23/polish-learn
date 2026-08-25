"""Pure progress rules, independent from HTTP, Django, and PostgreSQL."""

from datetime import date, timedelta
from typing import Optional


def next_streak(current: int, last_active_date: Optional[date], today: date) -> int:
    """Calculate the streak after completing a lesson on ``today``."""

    if current < 0:
        raise ValueError("current streak cannot be negative")

    if last_active_date == today:
        return current

    if last_active_date == today - timedelta(days=1):
        return current + 1

    return 1


def current_streak(active_dates: list[date], today: date) -> int:
    """Return the consecutive-day streak visible on ``today``.

    A streak remains visible until the end of the day after the latest activity,
    giving the learner the current day to continue it.
    """

    dates = sorted(set(active_dates), reverse=True)
    if not dates or dates[0] not in {today, today - timedelta(days=1)}:
        return 0

    streak = 1
    expected = dates[0] - timedelta(days=1)
    for active_date in dates[1:]:
        if active_date != expected:
            break
        streak += 1
        expected -= timedelta(days=1)
    return streak
