import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))

from ekta_runtime.upds_registry import DocumentRegistry, RegistryError  # noqa: E402


class UPDSRegistryTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "schemas").mkdir()
        (self.root / "upds" / "records").mkdir(parents=True)
        shutil.copy2(ROOT / "schemas" / "upds-document.schema.json", self.root / "schemas")
        shutil.copy2(
            ROOT / "upds" / "records" / "EKTA-DOC-000001.yml",
            self.root / "upds" / "records",
        )
        self.registry = DocumentRegistry(self.root)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_lists_valid_records_in_stable_id_order(self):
        items = self.registry.list_documents()
        self.assertEqual([item["id"] for item in items], ["EKTA-DOC-000001"])

    def test_gets_document_by_stable_id(self):
        item = self.registry.get_document("EKTA-DOC-000001")
        self.assertIsNotNone(item)
        self.assertEqual(item["title"], "UPDS document universe")

    def test_returns_none_for_unknown_id(self):
        self.assertIsNone(self.registry.get_document("EKTA-DOC-999999"))

    def test_rejects_duplicate_ids_across_record_files(self):
        source = self.root / "upds" / "records" / "EKTA-DOC-000001.yml"
        duplicate = self.root / "upds" / "records" / "duplicate.yml"
        duplicate.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
        with self.assertRaisesRegex(RegistryError, "duplicate"):
            self.registry.list_documents()

    def test_rejects_schema_invalid_record(self):
        path = self.root / "upds" / "records" / "EKTA-DOC-000001.yml"
        content = path.read_text(encoding="utf-8").replace("status: PROPOSED", "status: DONE")
        path.write_text(content, encoding="utf-8")
        with self.assertRaises(RegistryError):
            self.registry.list_documents()

    def test_rejects_malformed_yaml(self):
        path = self.root / "upds" / "records" / "broken.yml"
        path.write_text("record: [unterminated", encoding="utf-8")
        with self.assertRaisesRegex(RegistryError, "invalid YAML"):
            self.registry.list_documents()


if __name__ == "__main__":
    unittest.main()
