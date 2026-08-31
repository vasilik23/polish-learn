"""Honest, pressure-free insights for a learner's current daily goal."""

from dataclasses import dataclass
from statistics import median_low
from typing import Sequence


INSIGHT_PERIOD_DAYS = 28


@dataclass(frozen=True)
class DailyGoalInsight:
    period_days: int
    successful_days: int
    success_rate: int
    active_days: int
    typical_active_day_lessons: int
    status: str
    status_label: str
    recommendation: str


def build_daily_goal_insight(
    daily_completion_counts: Sequence[int],
    current_goal: int,
) -> DailyGoalInsight:
    """Compare the current goal with the last 28 calendar days.

    The profile stores no history of goal changes, so this deliberately answers
    the narrower question: how the *current* goal fits the available history.
    """

    goal = max(1, int(current_goal))
    counts = [max(0, int(count)) for count in daily_completion_counts[-INSIGHT_PERIOD_DAYS:]]
    if len(counts) < INSIGHT_PERIOD_DAYS:
        counts = [0] * (INSIGHT_PERIOD_DAYS - len(counts)) + counts

    active_counts = [count for count in counts if count > 0]
    active_days = len(active_counts)
    successful_days = sum(count >= goal for count in counts)
    success_rate = round(successful_days / INSIGHT_PERIOD_DAYS * 100)
    typical_lessons = median_low(active_counts) if active_counts else 0
    active_day_success_rate = (
        round(successful_days / active_days * 100) if active_days else 0
    )

    if active_days < 4:
        status = "collecting"
        status_label = "Пока мало данных"
        recommendation = (
            f"Сохрани цель {goal} на день ещё на несколько занятий — "
            "после этого подсказка станет точнее."
        )
    elif active_day_success_rate >= 70:
        status = "sustainable"
        status_label = "Нагрузка выглядит посильной"
        if successful_days >= INSIGHT_PERIOD_DAYS // 2:
            recommendation = (
                f"Можно оставить цель {goal}: текущий ритм её поддерживает. "
                "Повышать нагрузку стоит только если тебе комфортно."
            )
        else:
            recommendation = (
                f"В дни занятий цель {goal} обычно достигается. Лучше сохранить "
                "нагрузку и подобрать удобный ритм без гонки за серией."
            )
    elif active_day_success_rate >= 40:
        status = "developing"
        status_label = "Ритм ещё формируется"
        recommendation = (
            f"Можно пока оставить цель {goal} и оценить ещё две недели. "
            "Пропущенный день не обнуляет общий прогресс."
        )
    else:
        status = "demanding"
        status_label = "Цель выше привычного темпа"
        suggested_goal = min(goal, max(1, typical_lessons))
        if suggested_goal < goal:
            recommendation = (
                f"Если хочется более спокойного ритма, попробуй временно "
                f"{suggested_goal} в день. Текущую цель тоже можно оставить как ориентир."
            )
        else:
            recommendation = (
                "Сохрани минимальную цель и выбери удобные дни для занятий — "
                "регулярность можно наращивать постепенно."
            )

    return DailyGoalInsight(
        period_days=INSIGHT_PERIOD_DAYS,
        successful_days=successful_days,
        success_rate=success_rate,
        active_days=active_days,
        typical_active_day_lessons=typical_lessons,
        status=status,
        status_label=status_label,
        recommendation=recommendation,
    )
