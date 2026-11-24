#!/usr/bin/env python3
"""Validate that EKTA's chat-independent continuity package is complete."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_RELATIVE = Path("docs/PROJECT_CONTINUITY/CONTINUITY_MANIFEST.yml")
REQUIRED_PATHS = (
    "README.md",
    "docs/USER_DOCUMENTATION_INDEX.md",
    "docs/CONTEXT_CONTINUITY.md",
    "docs/MASTER_HANDOFF.md",
    "docs/PROJECT_STATE.md",
    "docs/ACTIVE_WORK.md",
    "docs/DECISION_REGISTER.md",
    "docs/CONSTRAINTS_AND_ASSUMPTIONS.md",
    "docs/OPEN_ISSUES.md",
    "docs/EVIDENCE_INDEX.md",
    "docs/SESSION_HANDOFF.md",
    "docs/INTEGRATION/UPDS_INTEGRATION_INDEX.md",
    "docs/PROJECT_CONTINUITY/CHAT_SESSION_ARCHIVE_2026-11-24.md",
    "docs/PROJECT_CONTINUITY/AGENT_ONBOARDING.md",
    "docs/PROJECT_CONTINUITY/RECOVERY_RUNBOOK.md",
    "docs/PROJECT_CONTINUITY/ORCHESTRATION_PLAN.md",
    "docs/PROJECT_CONTINUITY/CONTINUITY_MANIFEST.yml",
)


def _safe_file(root: Path, relative: str) -> bool:
    candidate = (root / relative).resolve()
    return candidate.is_relative_to(root.resolve()) and candidate.is_file()


def validate(root: Path | str = ROOT) -> list[str]:
    """Return continuity integrity issues; an empty list means structural PASS."""
    root = Path(root).resolve()
    errors: list[str] = []

    for relative in REQUIRED_PATHS:
        if not _safe_file(root, relative):
            errors.append(f"missing required file: {relative}")

    manifest_path = root / MANIFEST_RELATIVE
    if not manifest_path.is_file():
        return errors

    try:
        manifest: Any = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"invalid continuity manifest YAML: {exc}")
        return errors

    if not isinstance(manifest, dict):
        return errors + ["continuity manifest must be a YAML mapping"]

    for field in ("project_id", "canonical_repository", "archive", "canonical_entry_points", "recovery"):
        if field not in manifest:
            errors.append(f"continuity manifest missing field: {field}")

    archive = manifest.get("archive")
    if isinstance(archive, dict):
        archive_path = archive.get("path")
        fidelity = archive.get("fidelity", "")
        if not isinstance(archive_path, str) or not _safe_file(root, archive_path):
            errors.append("continuity archive path is missing or unsafe")
        if not isinstance(fidelity, str) or "verbatim_transcript" in fidelity.lower():
            errors.append("archive fidelity must disclose that this is not a verbatim transcript")

    entries = manifest.get("canonical_entry_points")
    if not isinstance(entries, list) or not entries:
        errors.append("canonical_entry_points must be a non-empty list")
    else:
        for entry in entries:
            if not isinstance(entry, str) or not _safe_file(root, entry):
                errors.append(f"missing manifest entry or unsafe path: {entry}")

    recovery = manifest.get("recovery")
    if not isinstance(recovery, dict) or recovery.get("clean_clone_required") is not True:
        errors.append("recovery.clean_clone_required must be true")

    return errors


def main() -> int:
    issues = validate()
    if issues:
        for issue in issues:
            print(f"ERROR: {issue}")
        return 1
    print(f"PASS: continuity package and {len(REQUIRED_PATHS)} required files validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
