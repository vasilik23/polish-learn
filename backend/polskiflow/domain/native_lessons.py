"""Safe lesson payloads and stateless answer evaluation for separate clients."""

import random
from dataclasses import dataclass

from polskiflow.content import flashcards, grammar, quiz, task


@dataclass(frozen=True)
class NativeLesson:
    metadata: dict
    theory: dict | None
    steps: list[dict]


class NativeLessonError(ValueError):
    pass


def build_native_lesson(lesson_id: str) -> NativeLesson | None:
    metadata = task(lesson_id)
    if metadata is None:
        return None
    kind = metadata["kind"]
    if kind in {"words", "review"}:
        steps = [
            {
                "position": position,
                "type": "flashcard",
                "polish": card["polish"],
                "translation": card["translation"],
                "example": card["example"],
            }
            for position, card in enumerate(flashcards(lesson_id))
        ]
        theory = None
    else:
        grammar_content = grammar(lesson_id) if kind == "grammar" else None
        questions = grammar_content["questions"] if grammar_content else quiz(lesson_id)
        steps = [_public_question(lesson_id, kind, position, question) for position, question in enumerate(questions)]
        theory = (
            {"title": grammar_content["title"], "sections": grammar_content["sections"]}
            if grammar_content else None
        )
    return NativeLesson(metadata, theory, steps)


def evaluate_native_answer(lesson_id: str, position: int, payload: dict) -> dict:
    lesson = build_native_lesson(lesson_id)
    if lesson is None:
        raise NativeLessonError("lesson_not_found")
    if lesson.metadata["kind"] in {"words", "review"}:
        raise NativeLessonError("self_assessed_lesson")
    questions = _questions(lesson_id, lesson.metadata["kind"])
    if isinstance(position, bool) or not isinstance(position, int) or not 0 <= position < len(questions):
        raise NativeLessonError("invalid_position")
    question = questions[position]
    correct_index = question["correct"]
    explanation = question["explanation"]
    if _is_builder(question, lesson.metadata["kind"]):
        if set(payload) != {"position", "token_order"}:
            raise NativeLessonError("invalid_payload")
        order = payload["token_order"]
        tokens = _builder_tokens(question, lesson_id, position)
        if not isinstance(order, list) or any(isinstance(item, bool) or not isinstance(item, int) for item in order) or sorted(order) != list(range(len(tokens))):
            raise NativeLessonError("invalid_token_order")
        answer = " ".join(tokens[index] for index in order)
        correct_sentence = question["options"][correct_index]
        return {"correct": answer == correct_sentence, "correct_sentence": correct_sentence, "explanation": explanation}
    if set(payload) != {"position", "selected_index"}:
        raise NativeLessonError("invalid_payload")
    selected = payload["selected_index"]
    if isinstance(selected, bool) or not isinstance(selected, int) or not 0 <= selected < len(question["options"]):
        raise NativeLessonError("invalid_selected_index")
    return {"correct": selected == correct_index, "correct_index": correct_index, "explanation": explanation}


def _questions(lesson_id: str, kind: str) -> list[dict]:
    content = grammar(lesson_id) if kind == "grammar" else None
    return content["questions"] if content else quiz(lesson_id)


def _public_question(lesson_id: str, kind: str, position: int, question: dict) -> dict:
    base = {"position": position, "prompt": question["prompt"]}
    if _is_builder(question, kind):
        return {**base, "type": "sentence_builder", "tokens": _builder_tokens(question, lesson_id, position)}
    return {**base, "type": "choice", "options": question["options"]}


def _is_builder(question: dict, kind: str) -> bool:
    if kind != "grammar":
        return False
    try:
        return len(question["options"][question["correct"]].split()) >= 4
    except (IndexError, KeyError, TypeError):
        return False


def _builder_tokens(question: dict, lesson_id: str, position: int) -> list[str]:
    answer = question["options"][question["correct"]]
    tokens = answer.split()
    shuffled = list(tokens)
    random.Random(f"{lesson_id}:{position}:{answer}").shuffle(shuffled)
    if shuffled == tokens and len(shuffled) > 1:
        shuffled = shuffled[1:] + shuffled[:1]
    return shuffled
