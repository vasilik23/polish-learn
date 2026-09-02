import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from polskiflow.domain.content_workflow import (
    ManifestError,
    build_preview,
    build_migration_scaffold,
    build_publish_plan,
    load_manifest,
    validate_manifest,
    write_migration_scaffold,
)


class Command(BaseCommand):
    help = "Validate a content draft and create a write-free preview or publish plan."

    def add_arguments(self, parser):
        parser.add_argument("manifest", help="Path to a UTF-8 JSON draft manifest.")
        parser.add_argument("--output", help="Write the artifact to this JSON file.")
        parser.add_argument(
            "--prepare-publish",
            action="store_true",
            help="Create a reviewed publish plan; still performs no database writes.",
        )
        parser.add_argument(
            "--generate-scaffold",
            action="store_true",
            help="Write non-executable paired migration review scaffolds to a new/empty directory.",
        )
        parser.add_argument("--expected-checksum", default="", help="Exact approved SHA-256.")
        parser.add_argument("--output-directory", help="New or empty directory for scaffolds.")
        parser.add_argument(
            "--approval-id",
            default="",
            help="Editorial approval/ticket ID required with --prepare-publish.",
        )

    def handle(self, *args, **options):
        scaffold = options["generate_scaffold"]
        if options["prepare_publish"] and scaffold:
            raise CommandError("Выберите только один режим: --prepare-publish или --generate-scaffold.")
        if options["approval_id"] and not (options["prepare_publish"] or scaffold):
            raise CommandError("--approval-id используется с publish-plan или scaffold.")
        if scaffold and (not options["output_directory"] or not options["expected_checksum"]):
            raise CommandError(
                "--generate-scaffold требует --output-directory и --expected-checksum."
            )
        if scaffold and options["output"]:
            raise CommandError("--output несовместим с --generate-scaffold.")
        try:
            result = validate_manifest(load_manifest(options["manifest"]))
            if scaffold:
                project_root = Path(__file__).resolve().parents[5]
                artifacts = build_migration_scaffold(
                    result, options["approval_id"], options["expected_checksum"]
                )
                output = write_migration_scaffold(
                    artifacts,
                    options["output_directory"],
                    (
                        project_root / "backend/polskiflow/learning/migrations",
                        project_root / "supabase/migrations",
                    ),
                )
                self.stdout.write(self.style.SUCCESS(f"Scaffold written to {output}"))
                return
            artifact = (
                build_publish_plan(result, options["approval_id"])
                if options["prepare_publish"]
                else build_preview(result)
            )
        except ManifestError as exc:
            raise CommandError(str(exc)) from exc

        rendered = json.dumps(artifact, ensure_ascii=False, indent=2, sort_keys=True)
        if output := options["output"]:
            path = Path(output)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(rendered + "\n", encoding="utf-8")
            self.stdout.write(self.style.SUCCESS(f"Artifact written to {path}"))
        else:
            self.stdout.write(rendered)
