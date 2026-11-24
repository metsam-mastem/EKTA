import tempfile
import unittest
from pathlib import Path
from ves_core import Project, VesService
from ves_storage import ConcurrentWriteError, SQLiteProjectStore


class SQLiteProjectStoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.store = SQLiteProjectStore(Path(self.temp.name) / "ves.sqlite3")
        self.project = Project.create("Storage Test")
        VesService(self.project).add_entity("hardware.mcu", "MCU", {"cores": 4})

    def tearDown(self):
        self.temp.cleanup()

    def test_save_and_load_preserves_project_model(self):
        saved_at = self.store.save(self.project)
        restored = self.store.load(self.project.id)
        self.assertIsNotNone(restored)
        self.assertEqual(restored.to_dict(), self.project.to_dict())
        self.assertTrue(saved_at)

    def test_optimistic_concurrency_rejects_stale_revision(self):
        self.store.save(self.project)
        with self.assertRaises(ConcurrentWriteError):
            self.store.save(self.project, expected_updated_at="stale-revision")

    def test_list_projects_returns_metadata_only(self):
        self.store.save(self.project)
        items = self.store.list_projects()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["id"], self.project.id)
        self.assertNotIn("payload", items[0])


if __name__ == "__main__":
    unittest.main()
