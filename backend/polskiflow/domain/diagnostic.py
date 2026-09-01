"""Deterministic self-assessment recommendations for the diagnostic route."""

from __future__ import annotations

from dataclasses import dataclass


LEVELS = ("A1", "A2", "B1", "B2", "C1", "C2")
MODES = (
    ("reception", "Восприятие", "понимание текстов и речи"),
    ("production", "Продукция", "устная и письменная речь"),
    ("interaction", "Взаимодействие", "диалог и переписка"),
    ("mediation", "Медиация", "передача смысла другим"),
)
MODE_OPTIONS = {
    "reception": (
        ("0", "A1 — узнаю знакомые слова в очень простой речи и тексте"),
        ("1", "A2 — понимаю короткие сообщения на повседневные темы"),
        ("2", "B1 — понимаю основную мысль ясной речи и связных текстов"),
        ("3", "B2 — понимаю аргументацию и детали сложных материалов"),
        ("4", "C1 — понимаю длинную сложную речь, включая неявный смысл"),
        ("5", "C2 — без труда понимаю почти любую речь и текст"),
    ),
    "production": (
        ("0", "A1 — называю себя, людей и предметы простыми фразами"),
        ("1", "A2 — кратко описываю повседневные дела и события"),
        ("2", "B1 — связно рассказываю об опыте, планах и мнениях"),
        ("3", "B2 — ясно и подробно развиваю позицию и аргументы"),
        ("4", "C1 — точно и гибко строю сложное устное или письменное высказывание"),
        ("5", "C2 — создаю свободную, точную и стилистически тонкую речь"),
    ),
    "interaction": (
        ("0", "A1 — отвечаю на простые вопросы, если собеседник помогает"),
        ("1", "A2 — поддерживаю короткий обмен в привычной ситуации"),
        ("2", "B1 — участвую без подготовки в разговоре на знакомую тему"),
        ("3", "B2 — активно обсуждаю идеи и поддерживаю свою позицию"),
        ("4", "C1 — гибко веду сложное общение в социальных и рабочих ситуациях"),
        ("5", "C2 — легко управляю тонким, быстрым и неоднозначным взаимодействием"),
    ),
    "mediation": (
        ("0", "A1 — передаю простые имена, числа и знакомые слова"),
        ("1", "A2 — пересказываю главную информацию из короткого сообщения"),
        ("2", "B1 — объясняю основные пункты понятного текста или разговора"),
        ("3", "B2 — обобщаю разные позиции и поясняю важные детали"),
        ("4", "C1 — перестраиваю сложную информацию под нужды адресата"),
        ("5", "C2 — точно синтезирую источники, сохраняя оттенки и регистр"),
    ),
}


@dataclass(frozen=True)
class DiagnosticResult:
    level: str
    focus_modes: tuple[str, ...]
    answers: tuple[tuple[str, str, str], ...]
    calculation: str


def score_diagnostic(raw_answers: dict[str, str]) -> DiagnosticResult:
    """Return a cautious recommendation from four valid self-ratings.

    The average is rounded down and capped at one CEFR step above the weakest
    mode. This keeps one strong skill from hiding a substantially weaker one.
    """

    mode_keys = tuple(key for key, _title, _description in MODES)
    if set(raw_answers) != set(mode_keys) or any(
        raw_answers[key] == "" for key in mode_keys
    ):
        raise ValueError("Нужно оценить все четыре режима.")

    try:
        scores = {key: int(raw_answers[key]) for key in mode_keys}
    except (TypeError, ValueError) as error:
        raise ValueError("Выберите один из предложенных уровней.") from error
    if any(score < 0 or score >= len(LEVELS) for score in scores.values()):
        raise ValueError("Выберите один из предложенных уровней.")

    average_floor = sum(scores.values()) // len(scores)
    weakest = min(scores.values())
    recommended_index = min(average_floor, weakest + 1)
    ordered_modes = sorted(
        MODES,
        key=lambda mode: (scores[mode[0]], mode_keys.index(mode[0])),
    )
    focus_modes = tuple(mode[1] for mode in ordered_modes[:2])
    answers = tuple(
        (title, LEVELS[scores[key]], description)
        for key, title, description in MODES
    )
    calculation = (
        f"Среднее с округлением вниз: {LEVELS[average_floor]}; "
        f"самый слабый режим: {LEVELS[weakest]}. Рекомендация не выше чем "
        "на одну ступень от самого слабого режима."
    )
    return DiagnosticResult(
        level=LEVELS[recommended_index],
        focus_modes=focus_modes,
        answers=answers,
        calculation=calculation,
    )
