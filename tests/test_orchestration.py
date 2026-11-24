import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_orchestration import validate_registry


class OrchestrationRegistryTests(unittest.TestCase):
    def test_current_registry_is_valid(self):
        self.assertEqual(validate_registry(), [])

    def test_duplicate_workstream_id_is_rejected(self):
        registry = yaml.safe_load((ROOT / "orchestration" / "WORKSTREAMS.yml").read_text(encoding="utf-8"))
        registry["workstreams"][1]["id"] = registry["workstreams"][0]["id"]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "registry.yml"
            path.write_text(yaml.safe_dump(registry, allow_unicode=True), encoding="utf-8")
            self.assertTrue(any("duplicate workstream id" in item for item in validate_registry(path)))

    def test_unknown_dependency_is_rejected(self):
        registry = yaml.safe_load((ROOT / "orchestration" / "WORKSTREAMS.yml").read_text(encoding="utf-8"))
        registry["workstreams"][0]["dependencies"] = ["WS-DOES-NOT-EXIST"]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "registry.yml"
            path.write_text(yaml.safe_dump(registry, allow_unicode=True), encoding="utf-8")
            self.assertTrue(any("unknown dependency" in item for item in validate_registry(path)))

    def test_dependency_cycle_is_rejected(self):
        registry = yaml.safe_load((ROOT / "orchestration" / "WORKSTREAMS.yml").read_text(encoding="utf-8"))
        registry["workstreams"][0]["dependencies"] = ["WS-UMSF"]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "registry.yml"
            path.write_text(yaml.safe_dump(registry, allow_unicode=True), encoding="utf-8")
            self.assertTrue(any("dependency cycle" in item for item in validate_registry(path)))


if __name__ == "__main__":
    unittest.main()
