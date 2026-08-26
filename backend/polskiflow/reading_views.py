"""Reading library and personal dictionary browser flows."""

import re

from django.http import Http404, HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from polskiflow.auth_views import require_browser_user
from polskiflow.content import reading_text, reading_texts
from polskiflow.dictionary_store import (
    delete_personal_word,
    load_personal_words,
    save_personal_word,
)
from polskiflow.progress_store import save_lesson_completion

TOKEN_PATTERN = re.compile(r"([\wąćęłńóśźżĄĆĘŁŃÓŚŹŻ-]+)", re.UNICODE)


@require_browser_user
def reading_library(request: HttpRequest) -> HttpResponse:
    return render(request, "reading/library.html", {"texts": reading_texts()})


@require_browser_user
def reader(request: HttpRequest, text_id: str) -> HttpResponse:
    text = reading_text(text_id)
    if text is None:
        raise Http404
    return render(
        request,
        "reading/reader.html",
        {"text": text, "paragraphs": _tokenize(text.paragraphs, text.glossary)},
    )


@require_browser_user
def dictionary(request: HttpRequest) -> HttpResponse:
    words = load_personal_words(
        request.supabase_access_token, request.supabase_user.id
    )
    return render(
        request,
        "reading/dictionary.html",
        {
            "words": words or [],
            "available": words is not None,
            "can_practice": len(words or []) >= 4,
            "needed_words": max(0, 4 - len(words or [])),
        },
    )


@require_browser_user
def dictionary_practice(request: HttpRequest) -> HttpResponse:
    words = load_personal_words(
        request.supabase_access_token, request.supabase_user.id
    )
    questions = _practice_questions(words or [])
    return render(
        request,
        "reading/practice.html",
        {
            "available": words is not None,
            "word_count": len(words or []),
            "question": questions[0] if questions else None,
            "total": len(questions),
            "index": 0,
            "score": 0,
            "selected": None,
        },
    )


@require_POST
@require_browser_user
def dictionary_practice_step(request: HttpRequest) -> HttpResponse:
    words = load_personal_words(
        request.supabase_access_token, request.supabase_user.id
    )
    questions = _practice_questions(words or [])
    try:
        index = int(request.POST.get("index", "0"))
        score = int(request.POST.get("score", "0"))
    except ValueError:
        return HttpResponseBadRequest("Некорректное состояние тренировки")
    if not questions or not 0 <= index < len(questions) or not 0 <= score <= index:
        return HttpResponseBadRequest("Некорректное состояние тренировки")
    action = request.POST.get("action", "")
    question = questions[index]
    if action == "answer":
        try:
            selected = int(request.POST["choice"])
        except (KeyError, ValueError):
            return HttpResponseBadRequest("Выберите ответ")
        if not 0 <= selected < len(question["options"]):
            return HttpResponseBadRequest("Некорректный ответ")
        context = _practice_context(questions, index, score, selected)
    elif action == "next":
        try:
            selected = int(request.POST["selected"])
        except (KeyError, ValueError):
            return HttpResponseBadRequest("Сначала ответьте")
        if not 0 <= selected < len(question["options"]):
            return HttpResponseBadRequest("Некорректный ответ")
        next_score = score + (selected == question["correct"])
        if index + 1 >= len(questions):
            saved = save_lesson_completion(
                request.supabase_access_token,
                request.supabase_user.id,
                "dictionary-practice",
                len(questions),
                next_score,
            )
            return render(
                request,
                "reading/_practice_complete.html",
                {"score": next_score, "total": len(questions), "saved": saved},
            )
        context = _practice_context(questions, index + 1, next_score, None)
    else:
        return HttpResponseBadRequest("Неизвестное действие")
    return render(request, "reading/_practice_question.html", context)


@require_POST
@require_browser_user
def add_dictionary_word(request: HttpRequest, text_id: str) -> HttpResponse:
    text = reading_text(text_id)
    if text is None:
        raise Http404
    word = request.POST.get("word", "").strip().casefold()
    translation = request.POST.get("translation", "").strip()
    context = request.POST.get("context", "").strip()
    expected_translation = {
        key.casefold(): value for key, value in text.glossary.items()
    }.get(word)
    if not word or translation != expected_translation or len(context) > 500:
        return HttpResponseBadRequest("Некорректное слово")
    saved = save_personal_word(
        request.supabase_access_token,
        request.supabase_user.id,
        word,
        translation,
        context,
        text.id,
    )
    return render(
        request,
        "reading/_save_status.html",
        {"saved": saved, "word": word},
    )


@require_POST
@require_browser_user
def remove_dictionary_word(request: HttpRequest, word_id: str) -> HttpResponse:
    deleted = delete_personal_word(
        request.supabase_access_token, request.supabase_user.id, word_id
    )
    if request.headers.get("HX-Request") == "true" and deleted:
        return HttpResponse("")
    return redirect("dictionary")


def _tokenize(paragraphs: list, glossary: dict) -> list[list[dict]]:
    translations = {key.casefold(): value for key, value in glossary.items()}
    result = []
    for paragraph in paragraphs if isinstance(paragraphs, list) else []:
        if not isinstance(paragraph, str):
            continue
        tokens = []
        for token in TOKEN_PATTERN.split(paragraph):
            if token:
                tokens.append(
                    {
                        "text": token,
                        "word": token.casefold(),
                        "translation": translations.get(token.casefold()),
                    }
                )
        result.append(tokens)
    return result


def _practice_questions(words: list[dict], limit: int = 10) -> list[dict]:
    usable = [
        word
        for word in words
        if isinstance(word.get("word"), str)
        and isinstance(word.get("translation"), str)
        and word["word"].strip()
        and word["translation"].strip()
    ]
    translations = list(dict.fromkeys(word["translation"] for word in usable))
    if len(translations) < 4:
        return []
    questions = []
    for index, word in enumerate(usable[:limit]):
        correct_translation = word["translation"]
        distractors = [item for item in translations if item != correct_translation][:3]
        if len(distractors) < 3:
            continue
        options = distractors + [correct_translation]
        correct = index % 4
        options[correct], options[-1] = options[-1], options[correct]
        questions.append(
            {
                "word": word["word"],
                "context": word.get("context") or "",
                "options": options,
                "correct": correct,
                "correct_answer": correct_translation,
            }
        )
    return questions


def _practice_context(
    questions: list[dict], index: int, score: int, selected: int | None
) -> dict:
    return {
        "question": questions[index],
        "index": index,
        "score": score,
        "selected": selected,
        "total": len(questions),
    }
