"""Reading library and personal dictionary browser flows."""

import re
from datetime import date
from urllib.parse import urlencode

from django.http import Http404, HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from polskiflow.auth_views import require_browser_user, select_cefr_level
from polskiflow.content import reading_text, reading_texts, task
from polskiflow.dictionary_store import (
    delete_personal_word,
    load_personal_words,
    save_personal_word,
    save_personal_word_review,
)
from polskiflow.domain.sm2 import DEFAULT_SM2_STATE, Sm2State, sm2_next
from polskiflow.progress_store import load_dashboard_progress, save_lesson_completion
from polskiflow.news_feed import CATEGORIES, CATEGORY_IDS, latest_official_news

TOKEN_PATTERN = re.compile(r"([\wąćęłńóśźżĄĆĘŁŃÓŚŹŻ-]+)", re.UNICODE)
REVIEW_QUALITIES = {"again", "hard", "good", "easy"}
PRACTICE_WORD_IDS_SESSION_KEY = "dictionary_practice_word_ids"
READING_LEVELS = ("A1", "A2", "B1", "B2", "C1")


@require_browser_user
def reading_library(request: HttpRequest) -> HttpResponse:
    selected_category = request.GET.get("category", "")
    if selected_category not in CATEGORY_IDS:
        selected_category = ""
    fallback_name = (request.supabase_user.email or "ученик").split("@", 1)[0]
    dashboard = load_dashboard_progress(
        request.supabase_access_token,
        request.supabase_user.id,
        fallback_name,
    )
    selected_level = select_cefr_level(request, dashboard.level)
    texts = reading_texts()
    for text in texts:
        if text.get("level") not in READING_LEVELS:
            text["level"] = "A1"
    level_tabs = [
        {
            "id": level,
            "href": f"?{urlencode({'level': level, **({'category': selected_category} if selected_category else {})})}#texts-title",
        }
        for level in READING_LEVELS
    ]
    news_categories = [
        {
            **category,
            "href": f"?{urlencode({'level': selected_level, 'category': category['id']})}#news-title",
        }
        for category in CATEGORIES
    ]
    return render(
        request,
        "reading/library.html",
        {
            "texts": [text for text in texts if text["level"] == selected_level],
            "reading_levels": level_tabs,
            "selected_reading_level": selected_level,
            "news": latest_official_news(category=selected_category or None),
            "news_categories": news_categories,
            "selected_news_category": selected_category,
        },
    )


@require_browser_user
def reader(request: HttpRequest, text_id: str) -> HttpResponse:
    text = reading_text(text_id)
    if text is None:
        raise Http404
    metadata = text.source_metadata if isinstance(text.source_metadata, dict) else {}
    comprehension_lesson_id = metadata.get("comprehension_lesson_id", "")
    comprehension_task = (
        task(comprehension_lesson_id)
        if isinstance(comprehension_lesson_id, str) and comprehension_lesson_id
        else None
    )
    return render(
        request,
        "reading/reader.html",
        {
            "text": text,
            "paragraphs": _tokenize(text.paragraphs, text.glossary),
            "comprehension_task": comprehension_task,
        },
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
    request.session[PRACTICE_WORD_IDS_SESSION_KEY] = [
        question["id"] for question in questions
    ]
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
    session_word_ids = request.session.get(PRACTICE_WORD_IDS_SESSION_KEY)
    questions = _practice_questions(
        words or [],
        word_ids=session_word_ids if isinstance(session_word_ids, list) else None,
    )
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
        quality = request.POST.get("quality", "")
        if quality not in REVIEW_QUALITIES:
            return HttpResponseBadRequest("Оцените, насколько легко вспомнилось слово")
        if selected != question["correct"]:
            quality = "again"
        now = timezone.now()
        state = Sm2State(
            ease_factor=float(question.get("ease_factor", 2.5)),
            interval_days=int(question.get("interval_days", 0)),
            repetitions=int(question.get("repetitions", 0)),
        )
        review = sm2_next(state, quality, now.date())
        review_saved = save_personal_word_review(
            request.supabase_access_token,
            request.supabase_user.id,
            question["id"],
            review,
            now.isoformat(),
        )
        next_score = score + (selected == question["correct"])
        if index + 1 >= len(questions):
            request.session.pop(PRACTICE_WORD_IDS_SESSION_KEY, None)
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
                {
                    "score": next_score,
                    "total": len(questions),
                    "saved": saved,
                    "review_saved": review_saved,
                },
            )
        context = _practice_context(questions, index + 1, next_score, None)
        context["review_saved"] = review_saved
    else:
        return HttpResponseBadRequest("Неизвестное действие")
    return render(request, "reading/_practice_question.html", context)


@require_POST
@require_browser_user
def add_dictionary_word(request: HttpRequest, text_id: str) -> HttpResponse:
    text = reading_text(text_id)
    if text is None:
        raise Http404
    surface_word = request.POST.get("word", "").strip().casefold()
    translation = request.POST.get("translation", "").strip()
    context = request.POST.get("context", "").strip()
    entry = _glossary_entries(text.glossary).get(surface_word)
    if (
        not entry
        or translation != entry["translation"]
        or len(context) > 500
    ):
        return HttpResponseBadRequest("Некорректное слово")
    word = entry["lemma"]
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
    entries = _glossary_entries(glossary)
    result = []
    for paragraph in paragraphs if isinstance(paragraphs, list) else []:
        if not isinstance(paragraph, str):
            continue
        tokens = []
        for token in TOKEN_PATTERN.split(paragraph):
            if token:
                entry = entries.get(token.casefold())
                tokens.append({"text": token, "word": token.casefold(), **(entry or {})})
        result.append(tokens)
    return result


def _glossary_entries(glossary: dict) -> dict[str, dict[str, str]]:
    """Normalize legacy translations and lemma-aware glossary entries."""
    if not isinstance(glossary, dict):
        return {}
    entries = {}
    for surface, value in glossary.items():
        if not isinstance(surface, str) or not surface.strip():
            continue
        if isinstance(value, str):
            translation = value.strip()
            lemma = surface.strip().casefold()
            part_of_speech = ""
        elif isinstance(value, dict):
            translation = value.get("translation", "")
            lemma = value.get("lemma", surface)
            part_of_speech = value.get("part_of_speech", "")
            if not all(isinstance(item, str) for item in (translation, lemma, part_of_speech)):
                continue
            translation = translation.strip()
            lemma = lemma.strip().casefold()
            part_of_speech = part_of_speech.strip()
        else:
            continue
        if translation and lemma:
            entries[surface.strip().casefold()] = {
                "translation": translation,
                "lemma": lemma,
                "part_of_speech": part_of_speech,
            }
    return entries


def _practice_questions(
    words: list[dict], limit: int = 10, word_ids: list[str] | None = None
) -> list[dict]:
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
    if word_ids is None:
        chosen_words = [word for word in usable if _is_due(word.get("next_review_date"))]
        chosen_words.sort(key=lambda word: word.get("next_review_date") or "")
    else:
        words_by_id = {str(word.get("id", "")): word for word in usable}
        chosen_words = [words_by_id[word_id] for word_id in word_ids if word_id in words_by_id]
    questions = []
    for index, word in enumerate(chosen_words[:limit]):
        correct_translation = word["translation"]
        distractors = [item for item in translations if item != correct_translation][:3]
        if len(distractors) < 3:
            continue
        options = distractors + [correct_translation]
        correct = index % 4
        options[correct], options[-1] = options[-1], options[correct]
        questions.append(
            {
                "id": str(word.get("id", "")),
                "word": word["word"],
                "context": word.get("context") or "",
                "options": options,
                "correct": correct,
                "correct_answer": correct_translation,
                "ease_factor": word.get("ease_factor", DEFAULT_SM2_STATE.ease_factor),
                "interval_days": word.get("interval_days", DEFAULT_SM2_STATE.interval_days),
                "repetitions": word.get("repetitions", DEFAULT_SM2_STATE.repetitions),
            }
        )
    return questions


def _is_due(value: object, today: date | None = None) -> bool:
    if value in (None, ""):
        return True
    if not isinstance(value, str):
        return True
    try:
        return date.fromisoformat(value) <= (today or timezone.now().date())
    except ValueError:
        return True


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
