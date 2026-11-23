import json
import sys
import unittest
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))

from ekta_runtime.content import split_front_matter


class ConceptSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads((ROOT / "schemas" / "concept.schema.json").read_text(encoding="utf-8"))
        cls.validator = jsonschema.Draft202012Validator(
            cls.schema, format_checker=jsonschema.FormatChecker()
        )

    def test_schema_is_valid_json_schema(self):
        jsonschema.Draft202012Validator.check_schema(self.schema)

    def test_all_current_concept_front_matter_matches_schema(self):
        for path in sorted((ROOT / "encyclopedia" / "concepts").glob("*.md")):
            metadata, _ = split_front_matter(path.read_text(encoding="utf-8"))
            with self.subTest(path=path.name):
                self.assertEqual(list(self.validator.iter_errors(metadata)), [])

    def test_invalid_status_is_rejected(self):
        candidate = {
            "id": "EKTA-CON-999999",
            "canonical_name": "Test Concept",
            "status": "DONE",
            "revision": "0.1.0",
            "created": "2026-11-23",
            "updated": "2026-11-23",
            "domains": ["software-engineering"],
            "layers": ["platform-runtime"],
            "knowledge_types": ["concept"],
            "aliases": [],
            "confidence": "medium",
            "sources": [],
        }
        self.assertTrue(list(self.validator.iter_errors(candidate)))


if __name__ == "__main__":
    unittest.main()
