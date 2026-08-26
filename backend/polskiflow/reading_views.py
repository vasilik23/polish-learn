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
        {"words": words or [], "available": words is not None},
    )


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
