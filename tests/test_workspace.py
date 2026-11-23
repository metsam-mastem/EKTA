import base64
import sys
import unittest
import zipfile
from io import BytesIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))

from fastapi.testclient import TestClient
from ekta_runtime.api import app


class WorkspaceApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_self_test_reports_runtime_and_repository_checks(self):
        response = self.client.get("/api/v1/workspace/self-test")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("checks", data)
        self.assertTrue(any(item["id"] == "repository" for item in data["checks"]))

    def test_documentation_center_lists_only_markdown_docs(self):
        response = self.client.get("/api/v1/workspace/docs")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(item["path"] == "docs/USER_MANUAL.md" for item in response.json()["items"]))

    def test_import_preview_is_staged_and_never_writes_canonical_content(self):
        response = self.client.post("/api/v1/workspace/import/preview", json={
            "filename": "sample.md",
            "content": "---\nid: SAMPLE\n---\n# Sample\nBody",
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "staged")
        self.assertFalse((ROOT / "encyclopedia" / "concepts" / "sample.md").exists())

    def test_import_rejects_unsupported_extensions_and_oversized_payloads(self):
        bad = self.client.post("/api/v1/workspace/import/preview", json={"filename":"x.exe","content":"x"})
        self.assertEqual(bad.status_code, 400)
        huge = self.client.post("/api/v1/workspace/import/preview", json={"filename":"x.md","content":"x"*(1024*1024+1)})
        self.assertEqual(huge.status_code, 413)

    def test_import_rejects_malformed_yaml(self):
        response = self.client.post("/api/v1/workspace/import/preview", json={
            "filename":"broken.yaml","content":"key: [unterminated"
        })
        self.assertEqual(response.status_code, 400)

    def test_editor_saves_a_draft_outside_canonical_encyclopedia(self):
        response = self.client.post("/api/v1/workspace/drafts", json={
            "id":"EKTA-CON-900001","canonical_name":"Draft concept","body":"## Definition\nDraft only"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["status"], "draft")
        self.assertFalse((ROOT / "encyclopedia" / "concepts" / "EKTA-CON-900001.md").exists())

    def test_editor_rejects_noncanonical_id_and_existing_canonical_id(self):
        invalid = self.client.post("/api/v1/workspace/drafts", json={
            "id":"NEW-CONCEPT","canonical_name":"Invalid","body":"Draft"
        })
        self.assertEqual(invalid.status_code, 400)
        duplicate = self.client.post("/api/v1/workspace/drafts", json={
            "id":"EKTA-CON-000001","canonical_name":"Runtime duplicate","body":"Draft"
        })
        self.assertEqual(duplicate.status_code, 409)

    def test_backup_is_created_and_restore_only_stages_archive(self):
        backup = self.client.post("/api/v1/workspace/backup")
        self.assertEqual(backup.status_code, 200)
        self.assertGreater(backup.json()["size"], 0)
        archive = BytesIO()
        with zipfile.ZipFile(archive, "w") as zf:
            zf.writestr("EKTA/README.md", "# safe")
        restore = self.client.post("/api/v1/workspace/restore/preview", json={
            "filename":"backup.zip","archive_base64":base64.b64encode(archive.getvalue()).decode()
        })
        self.assertEqual(restore.status_code, 200)
        self.assertEqual(restore.json()["status"], "staged")
        self.assertNotEqual((ROOT / "README.md").read_text(encoding="utf-8"), "# safe")

    def test_restore_rejects_path_traversal_archive(self):
        archive = BytesIO()
        with zipfile.ZipFile(archive, "w") as zf:
            zf.writestr("EKTA/../../README.md", "# unsafe")
        response = self.client.post("/api/v1/workspace/restore/preview", json={
            "filename":"unsafe.zip","archive_base64":base64.b64encode(archive.getvalue()).decode()
        })
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
