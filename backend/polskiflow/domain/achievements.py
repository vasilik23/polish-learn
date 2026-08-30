"""Deterministic achievement progress derived from existing learner data."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Achievement:
    id: str
    icon: str
    title: str
    description: str
    current: int
    target: int

    @property
    def unlocked(self) -> bool:
        return self.current >= self.target

    @property
    def progress_percent(self) -> int:
        return min(round(self.current / self.target * 100), 100)


def build_achievements(
    *, completed_lessons: int, streak_days: int, dictionary_count: int, active_days: int
) -> tuple[Achievement, ...]:
    """Return stable milestones without persisting duplicate progress state."""

    return (
        Achievement("first-step", "🌱", "Первый шаг", "Завершить первый урок", completed_lessons, 1),
        Achievement("momentum", "🚀", "Набираю темп", "Завершить 10 уроков", completed_lessons, 10),
        Achievement("fifty-lessons", "🏅", "Полсотни", "Завершить 50 уроков", completed_lessons, 50),
        Achievement("streak-three", "🔥", "Три дня подряд", "Заниматься 3 дня подряд", streak_days, 3),
        Achievement("streak-seven", "⚡", "Неделя в ритме", "Заниматься 7 дней подряд", streak_days, 7),
        Achievement("word-collector", "💎", "Собиратель слов", "Добавить 25 слов в словарь", dictionary_count, 25),
        Achievement("steady-month", "🗓️", "Устойчивый месяц", "Заниматься в 12 разные дни", active_days, 12),
    )
