import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from polskiflow.domain.content_workflow import (
    ManifestError,
    build_preview,
    build_publish_plan,
    load_manifest,
    validate_manifest,
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
            "--approval-id",
            default="",
            help="Editorial approval/ticket ID required with --prepare-publish.",
        )

    def handle(self, *args, **options):
        if options["approval_id"] and not options["prepare_publish"]:
            raise CommandError("--approval-id используется только с --prepare-publish.")
        try:
            result = validate_manifest(load_manifest(options["manifest"]))
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
