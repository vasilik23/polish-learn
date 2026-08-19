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
