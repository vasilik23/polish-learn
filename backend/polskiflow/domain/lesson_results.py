"""Validation and canonical hashing for offline lesson-result events."""

import hashlib
import json
import re
import uuid
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone


CONTRACT_VERSION = "1.0"
MAX_REQUEST_BYTES = 8_192
CLIENT_INSTANCE_PATTERN = re.compile(r"^[A-Za-z0-9._:-]{1,128}$")


class LessonResultValidationError(ValueError):
    pass


@dataclass(frozen=True)
class LessonResult:
    event_id: str
    lesson_id: str
    plan_date: str
    completed_at: str
    cards_total: int
    cards_known: int
    contract_version: str
    client_instance_id: str | None
    payload_hash: str

    def event_payload(self) -> dict:
        return {
            "event_id": self.event_id,
            "lesson_id": self.lesson_id,
            "plan_date": self.plan_date,
            "completed_at": self.completed_at,
            "cards_total": self.cards_total,
            "cards_known": self.cards_known,
            "contract_version": self.contract_version,
            "client_instance_id": self.client_instance_id,
        }


def validate_lesson_result(payload: object, *, today: date | None = None) -> LessonResult:
    if not isinstance(payload, dict):
        raise LessonResultValidationError("JSON body must be an object")
    allowed = {
        "event_id", "lesson_id", "plan_date", "completed_at", "cards_total",
        "cards_known", "contract_version", "client_instance_id",
    }
    unknown = set(payload) - allowed
    if unknown:
        raise LessonResultValidationError(f"Unsupported fields: {', '.join(sorted(unknown))}")
    required = allowed - {"client_instance_id"}
    missing = required - set(payload)
    if missing:
        raise LessonResultValidationError(f"Missing fields: {', '.join(sorted(missing))}")

    try:
        event_id = str(uuid.UUID(str(payload["event_id"])))
    except (ValueError, TypeError, AttributeError):
        raise LessonResultValidationError("event_id must be a UUID") from None
    lesson_id = payload["lesson_id"]
    if not isinstance(lesson_id, str) or not re.fullmatch(r"[a-z0-9-]{1,32}", lesson_id):
        raise LessonResultValidationError("lesson_id is invalid")
    if payload["contract_version"] != CONTRACT_VERSION:
        raise LessonResultValidationError("Unsupported contract_version")
    for field in ("cards_total", "cards_known"):
        if type(payload[field]) is not int or not 0 <= payload[field] <= 10_000:
            raise LessonResultValidationError(f"{field} must be an integer from 0 to 10000")
    if payload["cards_known"] > payload["cards_total"]:
        raise LessonResultValidationError("cards_known cannot exceed cards_total")
    try:
        plan_date = date.fromisoformat(payload["plan_date"])
    except (TypeError, ValueError):
        raise LessonResultValidationError("plan_date must be an ISO date") from None
    today = today or datetime.now(timezone.utc).date()
    if not today - timedelta(days=365) <= plan_date <= today:
        raise LessonResultValidationError("plan_date is outside the accepted range")
    try:
        completed_at = datetime.fromisoformat(payload["completed_at"].replace("Z", "+00:00"))
    except (AttributeError, TypeError, ValueError):
        raise LessonResultValidationError("completed_at must be an ISO datetime") from None
    if completed_at.tzinfo is None:
        raise LessonResultValidationError("completed_at must include a timezone")
    completed_at = completed_at.astimezone(timezone.utc)
    if completed_at.date() != plan_date:
        raise LessonResultValidationError("completed_at must fall on plan_date in UTC")
    if completed_at > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise LessonResultValidationError("completed_at cannot be in the future")
    client_instance_id = payload.get("client_instance_id")
    if client_instance_id is not None and (
        not isinstance(client_instance_id, str)
        or CLIENT_INSTANCE_PATTERN.fullmatch(client_instance_id) is None
    ):
        raise LessonResultValidationError("client_instance_id is invalid")

    normalized = {
        "event_id": event_id,
        "lesson_id": lesson_id,
        "plan_date": plan_date.isoformat(),
        "completed_at": completed_at.isoformat().replace("+00:00", "Z"),
        "cards_total": payload["cards_total"],
        "cards_known": payload["cards_known"],
        "contract_version": CONTRACT_VERSION,
        "client_instance_id": client_instance_id,
    }
    digest = hashlib.sha256(
        json.dumps(normalized, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return LessonResult(**normalized, payload_hash=digest)
