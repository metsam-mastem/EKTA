import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from upds_validation import validate_records  # noqa: E402


class UPDSValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads((ROOT / "schemas" / "upds-document.schema.json").read_text(encoding="utf-8"))

    def test_schema_definition_is_valid(self):
        from jsonschema import Draft202012Validator
        Draft202012Validator.check_schema(self.schema)

    def test_repository_sample_record_is_valid(self):
        import yaml
        sample_path = ROOT / "upds" / "records" / "EKTA-DOC-000001.yml"
        sample = yaml.safe_load(sample_path.read_text(encoding="utf-8"))
        self.assertEqual(validate_records([sample], self.schema), [])

    def test_accepts_valid_document_record(self):
        record = {
            "id": "EKTA-DOC-000001",
            "title": "UPDS document universe",
            "artifact_type": "document_catalog",
            "family": "documentation",
            "level": "L1",
            "domain": "systems-engineering",
            "project_id": "EKTA",
            "status": "PROPOSED",
            "version": "0.1.0",
            "owner": "project-owner",
            "classification": "internal",
            "applicability": "REQUIRED"
        }
        self.assertEqual(validate_records([record], self.schema), [])

    def test_rejects_missing_required_metadata(self):
        self.assertTrue(validate_records([{"id": "EKTA-DOC-000001"}], self.schema))

    def test_rejects_invalid_status(self):
        record = {
            "id": "EKTA-DOC-000001",
            "title": "Example",
            "artifact_type": "specification",
            "family": "architecture",
            "level": "L2",
            "domain": "systems-engineering",
            "project_id": "EKTA",
            "status": "DONE",
            "version": "0.1.0",
            "owner": "owner",
            "classification": "internal",
            "applicability": "REQUIRED"
        }
        self.assertTrue(validate_records([record], self.schema))

    def test_detects_duplicate_ids(self):
        record = {
            "id": "EKTA-DOC-000001",
            "title": "Example",
            "artifact_type": "specification",
            "family": "architecture",
            "level": "L2",
            "domain": "systems-engineering",
            "project_id": "EKTA",
            "status": "PROPOSED",
            "version": "0.1.0",
            "owner": "owner",
            "classification": "internal",
            "applicability": "REQUIRED"
        }
        self.assertTrue(any("duplicate" in e.lower() for e in validate_records([record, record], self.schema)))


if __name__ == "__main__":
    unittest.main()
