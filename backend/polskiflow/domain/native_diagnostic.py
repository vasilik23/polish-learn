"""Non-persistent diagnostic contract for separate clients."""

from polskiflow.domain.diagnostic import (
    CHECK_TASKS,
    LEVELS,
    MODE_OPTIONS,
    MODES,
    score_checked_tasks,
    score_diagnostic,
)


class NativeDiagnosticError(ValueError):
    pass


def build_native_diagnostic() -> dict:
    return {
        "disclaimer": (
            "Предварительная рекомендация для выбора старта; это не экзамен, "
            "сертификат или подтверждение уровня CEFR."
        ),
        "self_assessment": [
            {
                "id": key,
                "title": title,
                "description": description,
                "options": [
                    {"value": value, "label": label}
                    for value, label in MODE_OPTIONS[key]
                ],
            }
            for key, title, description in MODES
        ],
        "checked_tasks": [
            {
                "id": task["key"],
                "mode": task["mode"],
                "prompt": task["prompt"],
                "options": [
                    {"id": value, "text": label}
                    for value, label in task["options"]
                ],
            }
            for task in CHECK_TASKS
        ],
        "persistence": "none",
    }


def evaluate_native_diagnostic(payload: dict) -> dict:
    if set(payload) != {"self_ratings", "answers"}:
        raise NativeDiagnosticError("Use exactly self_ratings and answers")
    self_ratings = payload["self_ratings"]
    answers = payload["answers"]
    if not isinstance(self_ratings, dict) or not isinstance(answers, dict):
        raise NativeDiagnosticError("self_ratings and answers must be objects")
    if any(not isinstance(key, str) or not isinstance(value, str) for key, value in self_ratings.items()):
        raise NativeDiagnosticError("Self-assessment identifiers and values must be strings")
    if any(not isinstance(key, str) or not isinstance(value, str) for key, value in answers.items()):
        raise NativeDiagnosticError("Answer identifiers and values must be strings")
    try:
        self_result = score_diagnostic(self_ratings)
        checked_result = score_checked_tasks(answers)
    except ValueError as error:
        raise NativeDiagnosticError(str(error)) from error

    recommended_level = min(
        (self_result.level, checked_result.level), key=LEVELS.index
    )
    feedback = [
        {
            "task_id": task["key"],
            "correct": answers[task["key"]] == task["answer"],
            "correct_option_id": task["answer"],
            "explanation": task["explanation"],
        }
        for task in CHECK_TASKS
    ]
    return {
        "recommended_level": recommended_level,
        "self_assessment": {
            "level": self_result.level,
            "focus_modes": list(self_result.focus_modes),
            "calculation": self_result.calculation,
        },
        "checked_sample": {
            "level": checked_result.level,
            "correct": checked_result.correct,
            "total": checked_result.total,
            "mode_scores": [
                {"mode": mode, "correct": correct, "total": total}
                for mode, correct, total in checked_result.mode_scores
            ],
            "calculation": checked_result.calculation,
            "feedback": feedback,
        },
        "disclaimer": "Предварительная рекомендация; не экзамен и не сертификат CEFR.",
        "persisted": False,
    }
