"""Validation and release planning for course-content drafts.

This module deliberately has no database or network dependencies.  A reviewed
artifact is an input to the normal migration review, not a production writer.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


LEVELS = {"A1", "A2", "B1", "B2", "C1", "C2"}
STATUSES = {"draft", "review", "approved"}
ORIGINS = {"original", "external"}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CHECKSUM_RE = re.compile(r"^[0-9a-f]{64}$")
APPROVAL_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/-]{0,99}$")


class ManifestError(ValueError):
    """Raised when a draft cannot safely enter the editorial workflow."""


@dataclass(frozen=True)
class ValidationResult:
    manifest: dict[str, Any]
    counts: dict[str, int]
    warnings: tuple[str, ...]
    checksum: str


def load_manifest(path: str | Path) -> dict[str, Any]:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ManifestError(f"Не удалось прочитать JSON manifest: {exc}") from exc
    if not isinstance(value, dict):
        raise ManifestError("Корень manifest должен быть JSON-объектом.")
    return value


def _require_text(container: dict[str, Any], key: str, location: str) -> str:
    value = container.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ManifestError(f"{location}.{key}: требуется непустая строка.")
    return value.strip()


def _require_list(container: dict[str, Any], key: str, location: str) -> list[Any]:
    value = container.get(key)
    if not isinstance(value, list):
        raise ManifestError(f"{location}.{key}: требуется список.")
    return value


def _valid_iso_date(value: str) -> bool:
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def validate_manifest(manifest: dict[str, Any]) -> ValidationResult:
    if manifest.get("schema_version") != 1:
        raise ManifestError("schema_version: поддерживается только версия 1.")

    draft_id = _require_text(manifest, "id", "manifest")
    if not SLUG_RE.fullmatch(draft_id):
        raise ManifestError("manifest.id: используйте lowercase kebab-case.")
    _require_text(manifest, "title", "manifest")
    if manifest.get("level") not in LEVELS:
        raise ManifestError("manifest.level: ожидается A1, A2, B1, B2, C1 или C2.")
    if manifest.get("language") != "pl":
        raise ManifestError("manifest.language: учебный контент должен иметь значение pl.")
    if manifest.get("status") not in STATUSES:
        raise ManifestError("manifest.status: ожидается draft, review или approved.")

    source = manifest.get("source")
    if not isinstance(source, dict):
        raise ManifestError("manifest.source: требуется карточка источника.")
    origin = source.get("origin")
    if origin not in ORIGINS:
        raise ManifestError("source.origin: ожидается original или external.")
    _require_text(source, "license", "source")
    verified_at = _require_text(source, "verified_at", "source")
    if not _valid_iso_date(verified_at):
        raise ManifestError("source.verified_at: ожидается дата YYYY-MM-DD.")
    if origin == "original":
        if _require_text(source, "created_for", "source") != "PolskiFlow":
            raise ManifestError("source.created_for: оригинал должен быть создан для PolskiFlow.")
    else:
        for key in (
            "source_url",
            "source_item_id",
            "author",
            "license_url",
            "retrieved_at",
            "changes",
            "attribution",
            "reviewer",
        ):
            _require_text(source, key, "source")
        if source.get("status") != "approved":
            raise ManifestError("source.status: внешний объект можно готовить только со статусом approved.")
        if not _valid_iso_date(source["retrieved_at"]):
            raise ManifestError("source.retrieved_at: ожидается дата YYYY-MM-DD.")

    content = manifest.get("content")
    if not isinstance(content, dict):
        raise ManifestError("manifest.content: требуется объект содержимого темы.")
    units = _require_list(content, "active_units", "content")
    card_sets = _require_list(content, "card_sets", "content")
    exercises = _require_list(content, "exercises", "content")
    final_quiz = _require_list(content, "final_quiz", "content")
    grammar = content.get("grammar")
    reading = content.get("reading")
    if not isinstance(grammar, dict) or not grammar.get("summary"):
        raise ManifestError("content.grammar.summary: требуется грамматическое объяснение.")
    if not isinstance(reading, dict):
        raise ManifestError("content.reading: требуется объект чтения.")
    paragraphs = _require_list(reading, "paragraphs", "content.reading")
    glossary = reading.get("glossary")
    if not isinstance(glossary, dict) or not glossary:
        raise ManifestError("content.reading.glossary: требуется непустой glossary.")
    if any(not isinstance(item, list) for item in card_sets):
        raise ManifestError("content.card_sets: каждый набор должен быть списком карточек.")

    counts = {
        "active_units": len(units),
        "card_sets": len(card_sets),
        "flashcards": sum(len(item) for item in card_sets),
        "exercises": len(exercises),
        "reading_paragraphs": len(paragraphs),
        "glossary": len(glossary),
        "final_quiz": len(final_quiz),
    }
    expected = manifest.get("expected_counts")
    if not isinstance(expected, dict):
        raise ManifestError("manifest.expected_counts: зафиксируйте ожидаемые количества.")
    for key, actual in counts.items():
        if expected.get(key) != actual:
            raise ManifestError(
                f"expected_counts.{key}: указано {expected.get(key)!r}, фактически {actual}."
            )

    errors = []
    if not 12 <= counts["active_units"] <= 20:
        errors.append("active_units: требуется от 12 до 20 единиц.")
    if counts["card_sets"] != 2 or any(not 5 <= len(item) <= 8 for item in card_sets):
        errors.append("card_sets: требуется два набора по 5–8 карточек.")
    if counts["exercises"] < 5:
        errors.append("exercises: требуется минимум 5 заданий.")
    if counts["final_quiz"] < 8:
        errors.append("final_quiz: требуется минимум 8 вопросов.")
    if not paragraphs:
        errors.append("reading.paragraphs: чтение не может быть пустым.")
    if errors:
        raise ManifestError("\n".join(errors))

    warnings = ()
    if manifest["status"] != "approved":
        warnings = ("Черновик прошёл структурную проверку, но ещё не одобрен к публикации.",)
    canonical = json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return ValidationResult(
        manifest=manifest,
        counts=counts,
        warnings=warnings,
        checksum=hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
    )


def build_preview(result: ValidationResult) -> dict[str, Any]:
    manifest = result.manifest
    return {
        "artifact_type": "polskiflow-content-preview",
        "schema_version": 1,
        "draft": {
            "id": manifest["id"],
            "title": manifest["title"],
            "level": manifest["level"],
            "status": manifest["status"],
            "checksum": result.checksum,
        },
        "source": manifest["source"],
        "counts": result.counts,
        "warnings": list(result.warnings),
        "publishable": manifest["status"] == "approved",
        "boundary": "Preview only: no database, Supabase, migration or network write was performed.",
    }


def build_publish_plan(result: ValidationResult, approval_id: str) -> dict[str, Any]:
    if result.manifest["status"] != "approved":
        raise ManifestError("План публикации доступен только для status=approved.")
    review = result.manifest.get("review")
    if not isinstance(review, dict):
        raise ManifestError("manifest.review: для публикации требуется редакторская проверка.")
    for key in ("language_reviewer", "license_reviewer", "reviewed_at"):
        _require_text(review, key, "review")
    if not _valid_iso_date(review["reviewed_at"]):
        raise ManifestError("review.reviewed_at: ожидается дата YYYY-MM-DD.")
    if not approval_id.strip():
        raise ManifestError("approval_id: требуется идентификатор одобрения.")

    draft_id = result.manifest["id"]
    return {
        "artifact_type": "polskiflow-content-publish-plan",
        "schema_version": 1,
        "draft_id": draft_id,
        "manifest_checksum": result.checksum,
        "approval_id": approval_id.strip(),
        "counts": result.counts,
        "publish_boundary": {
            "writes_performed": False,
            "required_human_steps": [
                "Generate and review one ordered Django data migration from this exact checksum.",
                "Generate and review the matching rerunnable Supabase migration.",
                "Run tests, migration drift check, RLS/grant review, and preview.",
                "Apply only the reviewed Supabase migration, then deploy the matching commit.",
            ],
        },
        "rollback_plan": {
            "strategy": "forward-only corrective migration",
            "scope_key": draft_id,
            "steps": [
                "Disable records introduced by this draft using their stable IDs.",
                "Restore replaced content from the previous reviewed migration if applicable.",
                "Deploy the corrective Django and Supabase migrations together and verify counts.",
            ],
            "note": "Do not edit an applied migration or delete production rows manually.",
        },
    }


def require_publish_approval(
    result: ValidationResult, approval_id: str, expected_checksum: str
) -> str:
    """Verify the human approval boundary against the exact reviewed payload."""
    build_publish_plan(result, approval_id)
    if not APPROVAL_ID_RE.fullmatch(approval_id.strip()):
        raise ManifestError(
            "approval_id: используйте 1–100 букв, цифр или символов . _ : / -."
        )
    checksum = expected_checksum.strip().lower()
    if not CHECKSUM_RE.fullmatch(checksum):
        raise ManifestError("expected_checksum: ожидается полный SHA-256 из 64 символов.")
    if checksum != result.checksum:
        raise ManifestError(
            "expected_checksum: manifest изменился после проверки; запросите новое одобрение."
        )
    return approval_id.strip()


def build_migration_scaffold(
    result: ValidationResult, approval_id: str, expected_checksum: str
) -> dict[str, str]:
    """Build deterministic, deliberately non-executable migration review artifacts."""
    approval_id = require_publish_approval(result, approval_id, expected_checksum)
    manifest = result.manifest
    metadata = {
        "artifact_type": "polskiflow-content-migration-scaffold",
        "schema_version": 1,
        "draft_id": manifest["id"],
        "manifest_checksum": result.checksum,
        "approval_id": approval_id,
        "counts": result.counts,
        "files": {
            "payload": "approved-manifest.json",
            "django": "django-data-migration.scaffold.py",
            "supabase": "supabase-migration.scaffold.sql",
        },
        "writes_performed": False,
        "boundary": (
            "Review-only scaffold. It is not an ordered migration and contains no database "
            "operations. A developer must map the exact payload to current models/schema, "
            "review IDs, reverse/forward behavior, RLS and grants."
        ),
    }
    payload = json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    metadata_json = json.dumps(metadata, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    django = (
        '"""REVIEW SCAFFOLD ONLY — do not copy into migrations without completing TODOs.\n\n'
        f"Manifest: {result.checksum}\nApproval: {approval_id}\n"
        'This file intentionally performs no ORM or database operations.\n"""\n\n'
        f'MANIFEST_CHECKSUM = "{result.checksum}"\n'
        f"APPROVAL_ID = {approval_id!r}\n"
        f"DRAFT_ID = {manifest['id']!r}\n"
        'PAYLOAD_FILE = "approved-manifest.json"\n\n'
        "# TODO: choose the next ordered Django migration and its exact dependency.\n"
        "# TODO: map every payload object to current models using stable, reviewed IDs.\n"
        "# TODO: implement deterministic forwards and a safe forward-only correction plan.\n"
        "# TODO: add count, metadata, ordering, glossary and route regression tests.\n"
    )
    sql = (
        "-- REVIEW SCAFFOLD ONLY — contains no executable SQL.\n"
        f"-- Manifest: {result.checksum}\n"
        f"-- Approval: {approval_id}\n"
        f"-- Draft: {manifest['id']}\n"
        "-- Payload: approved-manifest.json\n\n"
        "-- TODO: choose the matching ordered Supabase migration filename.\n"
        "-- TODO: map stable IDs to the reviewed schema; use rerunnable operations where safe.\n"
        "-- TODO: review conflicts, rollback/correction behavior, RLS and grants.\n"
        "-- TODO: assert expected row counts before applying the reviewed migration.\n"
    )
    return {
        "scaffold.json": metadata_json,
        "approved-manifest.json": payload,
        "django-data-migration.scaffold.py": django,
        "supabase-migration.scaffold.sql": sql,
    }


def write_migration_scaffold(
    artifacts: dict[str, str], output_directory: str | Path, forbidden_directories: tuple[Path, ...]
) -> Path:
    """Write artifacts only to a new or empty directory outside real migration trees."""
    output = Path(output_directory).expanduser().resolve()
    forbidden = tuple(path.resolve() for path in forbidden_directories)
    if any(output == path or path in output.parents for path in forbidden):
        raise ManifestError("output_directory: нельзя писать scaffold в реальный каталог миграций.")
    if output.exists():
        if not output.is_dir():
            raise ManifestError("output_directory: ожидается каталог, а не файл.")
        if any(output.iterdir()):
            raise ManifestError("output_directory: каталог должен быть новым или пустым.")
    else:
        output.mkdir(parents=True)
    for filename, body in artifacts.items():
        target = (output / filename).resolve()
        if target.parent != output:
            raise ManifestError("Недопустимое имя scaffold-артефакта.")
        target.write_text(body, encoding="utf-8", newline="\n")
    return output
