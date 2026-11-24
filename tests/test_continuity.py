import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from validate_continuity import REQUIRED_PATHS, validate  # noqa: E402


class ContinuityValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        for relative in REQUIRED_PATHS:
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("placeholder\n", encoding="utf-8")
        manifest = {
            "project_id": "EKTA",
            "canonical_repository": "https://github.com/metsam-mastem/EKTA",
            "archive": {
                "path": "docs/PROJECT_CONTINUITY/CHAT_SESSION_ARCHIVE_2026-11-24.md",
                "fidelity": "structured_context_summary_not_verbatim_transcript",
            },
            "canonical_entry_points": list(REQUIRED_PATHS),
            "recovery": {"clean_clone_required": True},
        }
        path = self.root / "docs/PROJECT_CONTINUITY/CONTINUITY_MANIFEST.yml"
        path.write_text(yaml.safe_dump(manifest), encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_accepts_complete_continuity_package(self):
        self.assertEqual(validate(self.root), [])

    def test_rejects_missing_required_handoff_file(self):
        (self.root / "docs/SESSION_HANDOFF.md").unlink()
        self.assertTrue(any("missing required file" in issue for issue in validate(self.root)))

    def test_rejects_manifest_reference_to_missing_file(self):
        path = self.root / "docs/PROJECT_CONTINUITY/CONTINUITY_MANIFEST.yml"
        manifest = yaml.safe_load(path.read_text(encoding="utf-8"))
        manifest["canonical_entry_points"].append("docs/NOT_HERE.md")
        path.write_text(yaml.safe_dump(manifest), encoding="utf-8")
        self.assertTrue(any("missing manifest entry" in issue for issue in validate(self.root)))

    def test_rejects_manifest_without_chat_independent_recovery(self):
        path = self.root / "docs/PROJECT_CONTINUITY/CONTINUITY_MANIFEST.yml"
        manifest = yaml.safe_load(path.read_text(encoding="utf-8"))
        manifest["recovery"]["clean_clone_required"] = False
        path.write_text(yaml.safe_dump(manifest), encoding="utf-8")
        self.assertTrue(any("clean_clone_required" in issue for issue in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
