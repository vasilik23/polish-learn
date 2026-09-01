"""Deterministic, non-persistent recommendations for the diagnostic route."""

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

CHECK_TASKS = (
    {
        "key": "check_1",
        "mode": "Восприятие",
        "prompt": "Przeczytaj: «Sklep jest dziś otwarty do osiemnastej». Do której działa sklep?",
        "options": (("a", "Do 8:00"), ("b", "Do 18:00"), ("c", "Od 18:00")),
        "answer": "b",
        "explanation": "«Do osiemnastej» означает «до 18:00».",
    },
    {
        "key": "check_2",
        "mode": "Языковая форма",
        "prompt": "Выбери естественное завершение: «Codziennie rano ___ kawę».",
        "options": (("a", "piję"), ("b", "piłem"), ("c", "wypiję")),
        "answer": "a",
        "explanation": "Регулярное действие с «codziennie» выражено настоящим временем: «piję».",
    },
    {
        "key": "check_3",
        "mode": "Взаимодействие",
        "prompt": "Кто-то говорит: «Przepraszam, czy to miejsce jest wolne?». Как ответить, если место свободно?",
        "options": (("a", "Tak, proszę usiąść."), ("b", "Nie wiem, gdzie mieszkasz."), ("c", "Poproszę rachunek.")),
        "answer": "a",
        "explanation": "«Tak, proszę usiąść» прямо и вежливо приглашает занять свободное место.",
    },
    {
        "key": "check_4",
        "mode": "Медиация",
        "prompt": "Сообщение: «Spotkanie przeniesiono z wtorku na czwartek, godzina bez zmian». Что важно передать коллеге?",
        "options": (("a", "Встречу отменили."), ("b", "Встреча в четверг в прежнее время."), ("c", "Время встречи изменили.")),
        "answer": "b",
        "explanation": "Изменился день — со вторника на четверг, а время осталось прежним.",
    },
    {
        "key": "check_5",
        "mode": "Восприятие",
        "prompt": "«Mimo opóźnienia pociągu zdążyliśmy na przesiadkę». Что произошло?",
        "options": (("a", "Из-за опоздания пересадка не состоялась."), ("b", "Поезд не опоздал."), ("c", "Несмотря на опоздание, на пересадку успели.")),
        "answer": "c",
        "explanation": "Конструкция «mimo» вводит препятствие, которое не помешало результату.",
    },
    {
        "key": "check_6",
        "mode": "Языковая форма",
        "prompt": "Выбери вариант: «Gdybym wcześniej o tym wiedział, ___ ci pomóc».",
        "options": (("a", "mogę"), ("b", "mógłbym"), ("c", "będę mógł")),
        "answer": "b",
        "explanation": "Нереальное условие «gdybym wiedział» требует условной формы «mógłbym».",
    },
    {
        "key": "check_7",
        "mode": "Взаимодействие",
        "prompt": "Как вежливо не согласиться на рабочей встрече и оставить пространство для обсуждения?",
        "options": (("a", "To nie ma sensu."), ("b", "Nie masz racji."), ("c", "Rozumiem ten argument, jednak proponuję rozważyć też inne rozwiązanie.")),
        "answer": "c",
        "explanation": "Ответ признаёт аргумент собеседника, обозначает несогласие и предлагает альтернативу.",
    },
    {
        "key": "check_8",
        "mode": "Медиация",
        "prompt": "В отчёте сказано: «Wyniki są obiecujące, choć mała próba nie pozwala na uogólnienia». Как точнее пересказать вывод?",
        "options": (("a", "Результат окончательно доказан."), ("b", "Результаты перспективны, но из-за малой выборки вывод ограничен."), ("c", "Исследование не дало результатов.")),
        "answer": "b",
        "explanation": "Точный пересказ сохраняет и позитивный результат, и ограничение исследования.",
    },
)


@dataclass(frozen=True)
class DiagnosticResult:
    level: str
    focus_modes: tuple[str, ...]
    answers: tuple[tuple[str, str, str], ...]
    calculation: str


@dataclass(frozen=True)
class CheckedDiagnosticResult:
    level: str
    correct: int
    total: int
    answers: tuple[tuple[str, str, bool, str], ...]
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


def score_checked_tasks(raw_answers: dict[str, str]) -> CheckedDiagnosticResult:
    """Score the short observable sample; it deliberately cannot confirm CEFR."""

    keys = tuple(task["key"] for task in CHECK_TASKS)
    if set(raw_answers) != set(keys) or any(not raw_answers[key] for key in keys):
        raise ValueError("Нужно выполнить все восемь коротких заданий.")
    for task in CHECK_TASKS:
        allowed = {value for value, _label in task["options"]}
        if raw_answers[task["key"]] not in allowed:
            raise ValueError("Выберите один из предложенных вариантов ответа.")

    details = tuple(
        (
            task["mode"],
            task["prompt"],
            raw_answers[task["key"]] == task["answer"],
            task["explanation"],
        )
        for task in CHECK_TASKS
    )
    correct = sum(item[2] for item in details)
    # A short multiple-choice sample is deliberately capped at B2.
    if correct <= 2:
        level = "A1"
    elif correct <= 4:
        level = "A2"
    elif correct <= 6:
        level = "B1"
    else:
        level = "B2"
    calculation = (
        f"Верных ответов: {correct} из {len(CHECK_TASKS)}. Шкала старта: "
        "0–2 → A1, 3–4 → A2, 5–6 → B1, 7–8 → B2. "
        "Короткая проба не рекомендует уровень выше B2."
    )
    return CheckedDiagnosticResult(level, correct, len(CHECK_TASKS), details, calculation)
