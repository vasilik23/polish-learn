import json
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

from django.core.management import call_command
from django.test import SimpleTestCase


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
EXAMPLE_ROOT = REPOSITORY_ROOT / "docs" / "examples" / "content-workflow"
MANIFEST = EXAMPLE_ROOT / "time-meetings-approved.json"
RESOLUTIONS = EXAMPLE_ROOT / "time-meetings-resolutions.json"
APPROVAL_ID = "PILOT-TIME-001"
MANIFEST_CHECKSUM = "11c18422c41f6f80f995c7127445836e70d7202e51678b37578ecf12a2f27a94"
RESOLUTIONS_CHECKSUM = "e90d33273ce5fc14c288f4e49eac503bfc44fb43c7e458aa73a0888590fe5f45"


class ExistingTopicWorkflowPilotTests(SimpleTestCase):
    def test_time_meetings_review_chain_is_deterministic_and_write_free(self):
        django_migrations = REPOSITORY_ROOT / "backend" / "polskiflow" / "learning" / "migrations"
        supabase_migrations = REPOSITORY_ROOT / "supabase" / "migrations"
        migration_state = (
            tuple(path.name for path in django_migrations.iterdir()),
            tuple(path.name for path in supabase_migrations.iterdir()),
        )

        preview_stdout = StringIO()
        call_command("content_workflow", str(MANIFEST), stdout=preview_stdout)
        preview = json.loads(preview_stdout.getvalue())
        self.assertEqual(preview["draft"]["id"], "time-meetings")
        self.assertEqual(preview["draft"]["checksum"], MANIFEST_CHECKSUM)
        self.assertTrue(preview["publishable"])
        self.assertIn("no database, Supabase, migration or network write", preview["boundary"])

        with TemporaryDirectory() as directory:
            root = Path(directory)
            approval_path = root / "approval.json"
            call_command(
                "content_workflow",
                str(MANIFEST),
                check_resolutions=str(RESOLUTIONS),
                approval_id=APPROVAL_ID,
                expected_checksum=MANIFEST_CHECKSUM,
                output=str(approval_path),
            )
            approval = json.loads(approval_path.read_text(encoding="utf-8"))
            self.assertEqual(approval["approval_id"], APPROVAL_ID)
            self.assertEqual(approval["resolutions_checksum"], RESOLUTIONS_CHECKSUM)
            self.assertTrue(approval["complete"])
            self.assertFalse(approval["writes_performed"])

            scaffold_path = root / "scaffold"
            call_command(
                "content_workflow",
                str(MANIFEST),
                generate_scaffold=True,
                approval_id=APPROVAL_ID,
                expected_checksum=MANIFEST_CHECKSUM,
                output_directory=str(scaffold_path),
            )
            scaffold = json.loads((scaffold_path / "scaffold.json").read_text(encoding="utf-8"))
            self.assertEqual(scaffold["manifest_checksum"], MANIFEST_CHECKSUM)
            self.assertFalse(scaffold["writes_performed"])

            first_preview_path = root / "migration-preview-one"
            second_preview_path = root / "migration-preview-two"
            for output_path in (first_preview_path, second_preview_path):
                call_command(
                    "content_workflow",
                    str(MANIFEST),
                    generate_migration_preview=True,
                    model_resolutions=str(RESOLUTIONS),
                    approval_id=APPROVAL_ID,
                    expected_checksum=MANIFEST_CHECKSUM,
                    expected_resolutions_checksum=RESOLUTIONS_CHECKSUM,
                    output_directory=str(output_path),
                )

            expected_files = {
                "candidate-django-runpython.py",
                "candidate-supabase-content.sql",
                "migration-preview.json",
            }
            self.assertEqual({path.name for path in first_preview_path.iterdir()}, expected_files)
            for filename in expected_files:
                self.assertEqual(
                    (first_preview_path / filename).read_bytes(),
                    (second_preview_path / filename).read_bytes(),
                )
            migration_preview = json.loads(
                (first_preview_path / "migration-preview.json").read_text(encoding="utf-8")
            )
            self.assertEqual(migration_preview["manifest_checksum"], MANIFEST_CHECKSUM)
            self.assertEqual(migration_preview["resolutions_checksum"], RESOLUTIONS_CHECKSUM)
            self.assertFalse(migration_preview["writes_performed"])
            self.assertIn("Review artifact only", migration_preview["boundary"])

        self.assertEqual(
            migration_state,
            (
                tuple(path.name for path in django_migrations.iterdir()),
                tuple(path.name for path in supabase_migrations.iterdir()),
            ),
        )
