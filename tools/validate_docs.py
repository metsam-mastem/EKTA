#!/usr/bin/env python3
"""Lightweight EKTA repository validator; Python standard library only."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONCEPT_DIR = ROOT / "encyclopedia" / "concepts"
ID_RE = re.compile(r"^id:\s*(EKTA-[A-Z]+-\d{6})\s*$", re.M)
STATUS_RE = re.compile(r"^status:\s*(DRAFT|PROPOSED|RESEARCHED|VERIFIED|IMPLEMENTED|VALIDATED|DEPRECATED|BLOCKED|NOT_RUN)\s*$", re.M)
REQUIRED_HEADINGS = ("## Definition", "## Scope", "## Purpose", "## Role", "## Mechanism", "## Trade-offs", "## Verification")

def validate() -> list[str]:
    errors: list[str] = []
    seen: dict[str, Path] = {}
    for path in sorted(CONCEPT_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        ids = ID_RE.findall(text)
        if len(ids) != 1:
            errors.append(f"{path.relative_to(ROOT)}: expected exactly one stable EKTA ID")
        else:
            if ids[0] in seen:
                errors.append(f"duplicate ID {ids[0]}: {seen[ids[0]]} and {path}")
            seen[ids[0]] = path
        if not STATUS_RE.search(text):
            errors.append(f"{path.relative_to(ROOT)}: missing or invalid status")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"{path.relative_to(ROOT)}: missing heading {heading}")
        if not text.startswith("---\n"):
            errors.append(f"{path.relative_to(ROOT)}: missing YAML front matter")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_path = (path.parent / target.split("#", 1)[0]).resolve()
            if target.split("#", 1)[0] and not target_path.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link {target}")
    return errors

if __name__ == "__main__":
    problems = validate()
    if problems:
        print("\n".join(f"ERROR: {p}" for p in problems))
        sys.exit(1)
    print("PASS: EKTA documentation checks passed")
