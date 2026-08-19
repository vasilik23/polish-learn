"""Server-rendered lesson flows enhanced with HTMX."""

from django.http import Http404, HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_POST

from polskiflow.auth_views import require_browser_user
from polskiflow.content import FLASHCARDS, GRAMMAR, QUIZ, TASKS_BY_ID


@require_browser_user
def lesson(request: HttpRequest, lesson_id: str) -> HttpResponse:
    task = TASKS_BY_ID.get(lesson_id)
    if task is None:
        raise Http404
    context = {"task": task, "lesson_id": lesson_id}
    if lesson_id in {"words", "review"}:
        context.update(_flashcard_context(lesson_id, 0, 0, False))
    elif lesson_id == "grammar":
        context["grammar"] = GRAMMAR
    else:
        context.update(_question_context(lesson_id, 0, 0, None))
    return render(request, "lessons/page.html", context)


@require_POST
@require_browser_user
def lesson_step(request: HttpRequest, lesson_id: str) -> HttpResponse:
    if lesson_id not in TASKS_BY_ID:
        raise Http404
    try:
        index = int(request.POST.get("index", "0"))
        score = int(request.POST.get("score", "0"))
    except ValueError:
        return HttpResponseBadRequest("Некорректное состояние урока")
    action = request.POST.get("action", "")

    if lesson_id in {"words", "review"}:
        if not 0 <= index < len(FLASHCARDS) or not 0 <= score <= index:
            return HttpResponseBadRequest("Некорректное состояние урока")
        if action == "reveal":
            context = _flashcard_context(lesson_id, index, score, True)
        elif action in {"again", "know"}:
            next_score = score + (action == "know")
            if action == "again":
                context = _flashcard_context(lesson_id, index, score, False)
            elif index + 1 >= len(FLASHCARDS):
                return _complete(request, next_score, len(FLASHCARDS))
            else:
                context = _flashcard_context(lesson_id, index + 1, next_score, False)
        else:
            return HttpResponseBadRequest("Неизвестное действие")
        return render(request, "lessons/_flashcard.html", context)

    questions = GRAMMAR["questions"] if lesson_id == "grammar" else QUIZ
    if not 0 <= index < len(questions) or not 0 <= score <= index:
        return HttpResponseBadRequest("Некорректное состояние урока")
    if action == "start" and lesson_id == "grammar":
        context = _question_context(lesson_id, 0, 0, None)
    elif action == "answer":
        try:
            selected = int(request.POST["choice"])
        except (KeyError, ValueError):
            return HttpResponseBadRequest("Выберите ответ")
        if not 0 <= selected < len(questions[index]["options"]):
            return HttpResponseBadRequest("Некорректный ответ")
        context = _question_context(lesson_id, index, score, selected)
    elif action == "next":
        try:
            selected = int(request.POST["selected"])
        except (KeyError, ValueError):
            return HttpResponseBadRequest("Сначала ответьте")
        if not 0 <= selected < len(questions[index]["options"]):
            return HttpResponseBadRequest("Некорректный ответ")
        next_score = score + (selected == questions[index]["correct"])
        if index + 1 >= len(questions):
            return _complete(request, next_score, len(questions))
        context = _question_context(lesson_id, index + 1, next_score, None)
    else:
        return HttpResponseBadRequest("Неизвестное действие")
    return render(request, "lessons/_question.html", context)


def _flashcard_context(lesson_id: str, index: int, score: int, revealed: bool) -> dict:
    return {"lesson_id": lesson_id, "card": FLASHCARDS[index], "index": index, "score": score, "revealed": revealed, "total": len(FLASHCARDS)}


def _question_context(lesson_id: str, index: int, score: int, selected: int | None) -> dict:
    questions = GRAMMAR["questions"] if lesson_id == "grammar" else QUIZ
    return {"lesson_id": lesson_id, "question": questions[index], "index": index, "score": score, "selected": selected, "total": len(questions)}


def _complete(request: HttpRequest, score: int, total: int) -> HttpResponse:
    return render(request, "lessons/_complete.html", {"score": score, "total": total})
