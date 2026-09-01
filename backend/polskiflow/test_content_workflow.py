import json
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

from django.core.management import CommandError, call_command
from django.test import SimpleTestCase

from polskiflow.domain.content_workflow import (
    ManifestError,
    build_preview,
    build_publish_plan,
    validate_manifest,
)


def sample_manifest(*, status="draft", origin="original"):
    card_sets = [
        [{"id": f"card-a-{index}", "polish": f"wyraz {index}"} for index in range(5)],
        [{"id": f"card-b-{index}", "polish": f"zwrot {index}"} for index in range(5)],
    ]
    source = {
        "origin": origin,
        "license": "PolskiFlow original content",
        "verified_at": "2026-09-01",
        "created_for": "PolskiFlow",
    }
    if origin == "external":
        source = {
            "origin": "external",
            "source_url": "https://primary.example/item",
            "source_item_id": "item-42",
            "author": "Example Author",
            "license": "CC BY 4.0",
            "license_url": "https://creativecommons.org/licenses/by/4.0/",
            "verified_at": "2026-09-01",
            "retrieved_at": "2026-09-01",
            "changes": "Adapted into short exercises.",
            "attribution": "Example Author, CC BY 4.0.",
            "reviewer": "editor@example.invalid",
            "status": "approved",
        }
    return {
        "schema_version": 1,
        "id": "test-editorial-topic",
        "title": "Temat testowy",
        "level": "B1",
        "language": "pl",
        "status": status,
        "source": source,
        "content": {
            "active_units": [f"jednostka {index}" for index in range(12)],
            "card_sets": card_sets,
            "grammar": {"summary": "Krótkie i sprawdzalne wyjaśnienie."},
            "exercises": [{"prompt": f"Pytanie {index}"} for index in range(5)],
            "reading": {
                "paragraphs": ["Pierwszy akapit.", "Drugi akapit."],
                "glossary": {"akapit": {"lemma": "akapit", "translation": "абзац"}},
            },
            "final_quiz": [{"prompt": f"Quiz {index}"} for index in range(8)],
        },
        "expected_counts": {
            "active_units": 12,
            "card_sets": 2,
            "flashcards": 10,
            "exercises": 5,
            "reading_paragraphs": 2,
            "glossary": 1,
            "final_quiz": 8,
        },
    }


class ContentWorkflowDomainTests(SimpleTestCase):
    def test_draft_preview_is_validated_but_not_publishable(self):
        result = validate_manifest(sample_manifest())
        preview = build_preview(result)

        self.assertFalse(preview["publishable"])
        self.assertEqual(preview["counts"]["active_units"], 12)
        self.assertEqual(len(preview["draft"]["checksum"]), 64)
        self.assertIn("no database", preview["boundary"])

    def test_declared_counts_must_match_payload(self):
        manifest = sample_manifest()
        manifest["expected_counts"]["final_quiz"] = 9

        with self.assertRaisesRegex(ManifestError, "фактически 8"):
            validate_manifest(manifest)

    def test_external_source_requires_approved_object_card(self):
        manifest = sample_manifest(origin="external")
        manifest["source"]["status"] = "review"

        with self.assertRaisesRegex(ManifestError, "status.*approved"):
            validate_manifest(manifest)

    def test_publish_plan_requires_editorial_review_and_approval_id(self):
        manifest = sample_manifest(status="approved")
        result = validate_manifest(manifest)

        with self.assertRaisesRegex(ManifestError, "manifest.review"):
            build_publish_plan(result, "ED-101")

        manifest["review"] = {
            "language_reviewer": "language-editor",
            "license_reviewer": "rights-editor",
            "reviewed_at": "2026-09-01",
        }
        plan = build_publish_plan(validate_manifest(manifest), "ED-101")
        self.assertFalse(plan["publish_boundary"]["writes_performed"])
        self.assertEqual(plan["approval_id"], "ED-101")
        self.assertEqual(plan["rollback_plan"]["strategy"], "forward-only corrective migration")


class ContentWorkflowCommandTests(SimpleTestCase):
    def test_command_writes_preview_artifact_without_database(self):
        with TemporaryDirectory() as directory:
            manifest_path = Path(directory) / "draft.json"
            output_path = Path(directory) / "preview.json"
            manifest_path.write_text(
                json.dumps(sample_manifest(), ensure_ascii=False), encoding="utf-8"
            )

            stdout = StringIO()
            call_command(
                "content_workflow",
                str(manifest_path),
                output=str(output_path),
                stdout=stdout,
            )

            artifact = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(artifact["artifact_type"], "polskiflow-content-preview")
            self.assertIn("Artifact written", stdout.getvalue())

    def test_prepare_publish_rejects_unapproved_draft(self):
        with TemporaryDirectory() as directory:
            manifest_path = Path(directory) / "draft.json"
            manifest_path.write_text(json.dumps(sample_manifest()), encoding="utf-8")

            with self.assertRaisesRegex(CommandError, "status=approved"):
                call_command(
                    "content_workflow",
                    str(manifest_path),
                    prepare_publish=True,
                    approval_id="ED-101",
                )
