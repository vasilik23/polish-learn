import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from polskiflow.domain.content_workflow import (
    ManifestError,
    build_preview,
    build_migration_scaffold,
    build_publish_plan,
    load_manifest,
    validate_model_resolutions,
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
        parser.add_argument(
            "--check-resolutions",
            help="Validate a UTF-8 JSON model-resolution file without storage access.",
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
        resolution_path = options["check_resolutions"]
        selected_modes = sum(bool(value) for value in (options["prepare_publish"], scaffold, resolution_path))
        if selected_modes > 1:
            raise CommandError("Выберите только один режим публикации, scaffold или проверки resolutions.")
        if options["approval_id"] and not selected_modes:
            raise CommandError(
                "--approval-id используется с publish-plan, scaffold или проверкой resolutions."
            )
        if scaffold and (not options["output_directory"] or not options["expected_checksum"]):
            raise CommandError(
                "--generate-scaffold требует --output-directory и --expected-checksum."
            )
        if scaffold and options["output"]:
            raise CommandError("--output несовместим с --generate-scaffold.")
        if resolution_path and (not options["approval_id"] or not options["expected_checksum"]):
            raise CommandError(
                "--check-resolutions требует --approval-id и --expected-checksum."
            )
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
            if resolution_path:
                artifact = validate_model_resolutions(
                    result,
                    load_manifest(resolution_path),
                    options["approval_id"],
                    options["expected_checksum"],
                )
            else:
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
