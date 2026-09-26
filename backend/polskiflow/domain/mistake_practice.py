"""Signed state for the owner-scoped mistake practice flow."""

from dataclasses import dataclass

from django.core import signing
from django.utils.crypto import salted_hmac


SALT = "polskiflow.mistake-practice.v1"


class InvalidMistakePracticeState(ValueError):
    pass


@dataclass(frozen=True)
class MistakePracticeState:
    lesson_id: str
    position: int


def sign_mistake(user_id: str, lesson_id: str, position: int) -> str:
    owner = salted_hmac(SALT, user_id).hexdigest()[:32]
    return signing.dumps(
        {"v": 1, "owner": owner, "lesson": lesson_id, "position": position},
        salt=SALT,
        compress=True,
    )


def load_mistake(token: str, user_id: str) -> MistakePracticeState:
    try:
        payload = signing.loads(token, salt=SALT, max_age=12 * 60 * 60)
    except signing.BadSignature as error:
        raise InvalidMistakePracticeState from error
    expected_owner = salted_hmac(SALT, user_id).hexdigest()[:32]
    if (
        not isinstance(payload, dict)
        or set(payload) != {"v", "owner", "lesson", "position"}
        or payload["v"] != 1
        or payload["owner"] != expected_owner
        or not isinstance(payload["lesson"], str)
        or type(payload["position"]) is not int
        or payload["position"] < 0
    ):
        raise InvalidMistakePracticeState
    return MistakePracticeState(payload["lesson"], payload["position"])
