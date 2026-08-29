"""Server-rendered lesson flows enhanced with HTMX."""

import json
import random

from django.http import Http404, HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_POST

from polskiflow.auth_views import require_browser_user
from polskiflow.content import flashcards, grammar, quiz, task
from polskiflow.progress_store import save_lesson_completion


@require_browser_user
def lesson(request: HttpRequest, lesson_id: str) -> HttpResponse:
    lesson_task = task(lesson_id)
    if lesson_task is None:
        raise Http404
    lesson_kind = lesson_task["kind"]
    context = {"task": lesson_task, "lesson_id": lesson_id, "lesson_kind": lesson_kind}
    if lesson_kind in {"words", "review"}:
        context.update(_flashcard_context(lesson_id, lesson_kind, 0, 0, False))
    elif lesson_kind == "grammar":
        context["grammar"] = grammar(lesson_id)
    else:
        context.update(_question_context(lesson_id, lesson_kind, 0, 0, None))
    return render(request, "lessons/page.html", context)


@require_POST
@require_browser_user
def lesson_step(request: HttpRequest, lesson_id: str) -> HttpResponse:
    lesson_task = task(lesson_id)
    if lesson_task is None:
        raise Http404
    lesson_kind = lesson_task["kind"]
    try:
        index = int(request.POST.get("index", "0"))
        score = int(request.POST.get("score", "0"))
    except ValueError:
        return HttpResponseBadRequest("Некорректное состояние урока")
    action = request.POST.get("action", "")

    if lesson_kind in {"words", "review"}:
        cards = _lesson_flashcards(lesson_id, lesson_kind)
        if not 0 <= index < len(cards) or not 0 <= score <= index:
            return HttpResponseBadRequest("Некорректное состояние урока")
        if action == "reveal":
            context = _flashcard_context(lesson_id, lesson_kind, index, score, True)
        elif action in {"again", "know"}:
            next_score = score + (action == "know")
            if action == "again":
                context = _flashcard_context(lesson_id, lesson_kind, index, score, False)
            elif index + 1 >= len(cards):
                return _complete(request, lesson_id, next_score, len(cards))
            else:
                context = _flashcard_context(
                    lesson_id, lesson_kind, index + 1, next_score, False
                )
        else:
            return HttpResponseBadRequest("Неизвестное действие")
        return render(request, "lessons/_flashcard.html", context)

    grammar_content = grammar(lesson_id)
    questions = (
        grammar_content["questions"]
        if lesson_kind == "grammar" and grammar_content
        else quiz(lesson_id)
    )
    if not 0 <= index < len(questions) or not 0 <= score <= index:
        return HttpResponseBadRequest("Некорректное состояние урока")
    if action == "start" and lesson_kind == "grammar":
        context = _question_context(lesson_id, lesson_kind, 0, 0, None)
    elif action == "answer":
        if _is_sentence_builder(questions[index], lesson_kind):
            answer_order = _validated_builder_order(
                request.POST.get("answer_order", ""), questions[index], lesson_id, index
            )
            if answer_order is None:
                return HttpResponseBadRequest("Составьте предложение из всех слов")
            context = _question_context(
                lesson_id, lesson_kind, index, score, None, answer_order
            )
            return render(request, "lessons/_question.html", context)
        try:
            selected = int(request.POST["choice"])
        except (KeyError, ValueError):
            return HttpResponseBadRequest("Выберите ответ")
        if not 0 <= selected < len(questions[index]["options"]):
            return HttpResponseBadRequest("Некорректный ответ")
        context = _question_context(lesson_id, lesson_kind, index, score, selected)
    elif action == "next":
        if _is_sentence_builder(questions[index], lesson_kind):
            answer_order = _validated_builder_order(
                request.POST.get("answer_order", ""), questions[index], lesson_id, index
            )
            if answer_order is None:
                return HttpResponseBadRequest("Некорректный ответ")
            next_score = score + _builder_is_correct(
                answer_order, questions[index], lesson_id, index
            )
            if index + 1 >= len(questions):
                return _complete(request, lesson_id, next_score, len(questions))
            context = _question_context(
                lesson_id, lesson_kind, index + 1, next_score, None
            )
            return render(request, "lessons/_question.html", context)
        try:
            selected = int(request.POST["selected"])
        except (KeyError, ValueError):
            return HttpResponseBadRequest("Сначала ответьте")
        if not 0 <= selected < len(questions[index]["options"]):
            return HttpResponseBadRequest("Некорректный ответ")
        next_score = score + (selected == questions[index]["correct"])
        if index + 1 >= len(questions):
            return _complete(request, lesson_id, next_score, len(questions))
        context = _question_context(
            lesson_id, lesson_kind, index + 1, next_score, None
        )
    else:
        return HttpResponseBadRequest("Неизвестное действие")
    return render(request, "lessons/_question.html", context)


def _lesson_flashcards(lesson_id: str, lesson_kind: str) -> list[dict]:
    return flashcards(lesson_id)


def _flashcard_context(
    lesson_id: str,
    lesson_kind: str,
    index: int,
    score: int,
    revealed: bool,
) -> dict:
    cards = _lesson_flashcards(lesson_id, lesson_kind)
    if not cards:
        raise Http404
    return {
        "lesson_id": lesson_id,
        "lesson_kind": lesson_kind,
        "card": cards[index],
        "index": index,
        "score": score,
        "revealed": revealed,
        "total": len(cards),
    }


def _question_context(
    lesson_id: str,
    lesson_kind: str,
    index: int,
    score: int,
    selected: int | None,
    builder_answer: list[int] | None = None,
) -> dict:
    grammar_content = grammar(lesson_id)
    questions = (
        grammar_content["questions"]
        if lesson_kind == "grammar" and grammar_content
        else quiz(lesson_id)
    )
    if not questions:
        raise Http404
    context = {
        "lesson_id": lesson_id,
        "lesson_kind": lesson_kind,
        "question": questions[index],
        "index": index,
        "score": score,
        "selected": selected,
        "total": len(questions),
    }
    if _is_sentence_builder(questions[index], lesson_kind):
        tokens = _builder_tokens(questions[index], lesson_id, index)
        context.update(
            {
                "sentence_builder": True,
                "builder_tokens": tokens,
                "builder_answer": builder_answer,
                "builder_answer_json": json.dumps(builder_answer or []),
                "builder_answer_words": (
                    [tokens[token_index] for token_index in builder_answer]
                    if builder_answer is not None
                    else []
                ),
                "builder_correct": (
                    _builder_is_correct(builder_answer, questions[index], lesson_id, index)
                    if builder_answer is not None
                    else False
                ),
                "builder_correct_sentence": questions[index]["options"][questions[index]["correct"]],
            }
        )
    return context


def _is_sentence_builder(question: dict, lesson_kind: str) -> bool:
    """Use sentence assembly for grammar answers that are complete phrases."""
    if lesson_kind != "grammar":
        return False
    try:
        answer = question["options"][question["correct"]]
    except (IndexError, KeyError, TypeError):
        return False
    return isinstance(answer, str) and len(answer.split()) >= 4


def _builder_tokens(question: dict, lesson_id: str, index: int) -> list[str]:
    answer = question["options"][question["correct"]]
    tokens = answer.split()
    shuffled = list(tokens)
    random.Random(f"{lesson_id}:{index}:{answer}").shuffle(shuffled)
    if shuffled == tokens and len(shuffled) > 1:
        shuffled = shuffled[1:] + shuffled[:1]
    return shuffled


def _validated_builder_order(
    raw_order: str, question: dict, lesson_id: str, index: int
) -> list[int] | None:
    if len(raw_order) > 1024:
        return None
    try:
        order = json.loads(raw_order)
    except (TypeError, json.JSONDecodeError):
        return None
    tokens = _builder_tokens(question, lesson_id, index)
    if (
        not isinstance(order, list)
        or any(type(item) is not int for item in order)
        or sorted(order) != list(range(len(tokens)))
    ):
        return None
    return order


def _builder_is_correct(
    order: list[int], question: dict, lesson_id: str, index: int
) -> bool:
    tokens = _builder_tokens(question, lesson_id, index)
    assembled = " ".join(tokens[token_index] for token_index in order)
    correct = question["options"][question["correct"]]
    return assembled == correct


def _complete(request: HttpRequest, lesson_id: str, score: int, total: int) -> HttpResponse:
    saved = save_lesson_completion(
        request.supabase_access_token,
        request.supabase_user.id,
        lesson_id,
        total,
        score,
    )
    return render(
        request,
        "lessons/_complete.html",
        {"score": score, "total": total, "saved": saved},
    )
