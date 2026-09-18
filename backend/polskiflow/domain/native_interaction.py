"""Safe interaction and mediation contracts for native clients."""

from polskiflow.domain.interaction_scenarios import (
    FREE_PRODUCTION_SCENARIOS,
    SCENARIOS,
    SEQUENCE_SCENARIOS,
    validate_answer,
    validate_sequence_answer,
)


class NativeInteractionError(ValueError):
    pass


def build_native_interaction() -> dict:
    """Serialize prompts without exposing answer keys or explanations."""
    choice = [
        {
            "id": item.id,
            "kind": "choice",
            "level": item.level,
            "mode": item.mode,
            "title": item.title,
            "situation": item.situation,
            "prompt": item.prompt,
            "options": [{"id": option.id, "text": option.text} for option in item.options],
        }
        for item in SCENARIOS
    ]
    sequence = [
        {
            "id": item.id,
            "kind": "sequence",
            "level": item.level,
            "mode": item.mode,
            "title": item.title,
            "situation": item.situation,
            "prompt": item.prompt,
            "blocks": [{"id": block.id, "text": block.text} for block in item.blocks],
        }
        for item in SEQUENCE_SCENARIOS
    ]
    free_production = [
        {
            "id": item.id,
            "kind": "free_production",
            "level": item.level,
            "mode": item.mode,
            "title": item.title,
            "situation": item.situation,
            "task": item.task,
            "checklist": list(item.checklist),
            "submission": "local_only",
        }
        for item in FREE_PRODUCTION_SCENARIOS
    ]
    return {
        "scenarios": choice + sequence + free_production,
        "scenario_count": len(choice) + len(sequence) + len(free_production),
    }


def evaluate_native_interaction(scenario_id: str, payload: dict) -> dict:
    if scenario_id in {item.id for item in FREE_PRODUCTION_SCENARIOS}:
        raise NativeInteractionError("Free-production drafts stay on the device and are not submitted")

    if set(payload) == {"option_id"}:
        option_id = payload["option_id"]
        if not isinstance(option_id, str) or not option_id or len(option_id) > 40:
            raise NativeInteractionError("option_id must contain 1..40 characters")
        try:
            scenario, correct = validate_answer(scenario_id, option_id)
        except ValueError as error:
            if scenario_id not in {item.id for item in SCENARIOS}:
                raise NativeInteractionError("scenario_not_found") from error
            raise NativeInteractionError(str(error)) from error
        return {
            "scenario_id": scenario.id,
            "kind": "choice",
            "correct": correct,
            "correct_option_id": scenario.correct_option_id,
            "explanation": scenario.explanation,
        }

    if set(payload) == {"block_ids"}:
        block_ids = payload["block_ids"]
        if (
            not isinstance(block_ids, list)
            or any(not isinstance(item, str) or not item or len(item) > 40 for item in block_ids)
        ):
            raise NativeInteractionError("block_ids must be an array of short identifiers")
        try:
            scenario, correct = validate_sequence_answer(scenario_id, tuple(block_ids))
        except ValueError as error:
            if scenario_id not in {item.id for item in SEQUENCE_SCENARIOS}:
                raise NativeInteractionError("scenario_not_found") from error
            raise NativeInteractionError(str(error)) from error
        return {
            "scenario_id": scenario.id,
            "kind": "sequence",
            "correct": correct,
            "correct_order": list(scenario.correct_order),
            "explanation": scenario.explanation,
        }

    raise NativeInteractionError("Use exactly option_id or block_ids")
