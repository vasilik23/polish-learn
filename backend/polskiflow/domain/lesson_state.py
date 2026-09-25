"""Signed, user-bound state for server-rendered lesson flows."""

from dataclasses import dataclass

from django.core import signing
from django.utils.crypto import salted_hmac


SALT = "polskiflow.lesson-state.v1"
MAX_AGE_SECONDS = 12 * 60 * 60


class InvalidLessonState(ValueError):
    pass


@dataclass(frozen=True)
class LessonState:
    index: int
    score: int
    phase: str


def _owner_binding(user_id: str) -> str:
    return salted_hmac(SALT, user_id).hexdigest()[:32]


def sign_lesson_state(user_id: str, lesson_id: str, lesson_kind: str, index: int, score: int, phase: str = "ready") -> str:
    return signing.dumps(
        {"v": 1, "owner": _owner_binding(user_id), "lesson": lesson_id, "kind": lesson_kind, "index": index, "score": score, "phase": phase},
        salt=SALT,
        compress=True,
    )


def load_lesson_state(token: str, user_id: str, lesson_id: str, lesson_kind: str) -> LessonState:
    try:
        payload = signing.loads(token, salt=SALT, max_age=MAX_AGE_SECONDS)
    except signing.BadSignature as error:
        raise InvalidLessonState from error
    if not isinstance(payload, dict) or set(payload) != {"v", "owner", "lesson", "kind", "index", "score", "phase"}:
        raise InvalidLessonState
    index, score = payload["index"], payload["score"]
    if (
        payload["v"] != 1 or payload["owner"] != _owner_binding(user_id)
        or payload["lesson"] != lesson_id or payload["kind"] != lesson_kind
        or type(index) is not int or type(score) is not int
        or index < 0 or score < 0 or score > index + (payload["phase"] == "answered")
        or payload["phase"] not in {"ready", "answered"}
    ):
        raise InvalidLessonState
    return LessonState(index=index, score=score, phase=payload["phase"])
