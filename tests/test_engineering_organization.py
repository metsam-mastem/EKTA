"""Regression tests for the engineering organization crosswalk."""
from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_engineering_organization",
    ROOT / "tools" / "validate_engineering_organization.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class EngineeringOrganizationTests(unittest.TestCase):
    def test_crosswalk_passes_validation(self):
        self.assertEqual(MODULE.validate(), [])

    def test_registry_does_not_replace_canonical_taxonomy(self):
        data = json.loads(
            (ROOT / "taxonomy" / "ENGINEERING_ORGANIZATION_VIEW.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(
            data["classification_policy"]["macro_view_role"], "crosswalk_only"
        )
        self.assertTrue(data["classification_policy"]["no_new_territory_ids"])

    def test_fourteen_macro_areas_are_present(self):
        data = json.loads(
            (ROOT / "taxonomy" / "ENGINEERING_ORGANIZATION_VIEW.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(len(data["macro_areas"]), 14)


if __name__ == "__main__":
    unittest.main()
