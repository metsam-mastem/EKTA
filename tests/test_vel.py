import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))

from ekta_runtime.vel import canonical_json, load_model, to_dot, validate_model


class VELModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example_path = ROOT / "projects" / "vel" / "examples" / "local-ai-workstation.json"
        cls.model = load_model(cls.example_path)

    def test_example_has_no_semantic_findings(self):
        self.assertEqual(validate_model(self.model), [])

    def test_duplicate_node_id_is_reported(self):
        model = json.loads(json.dumps(self.model))
        model["nodes"].append(json.loads(json.dumps(model["nodes"][0])))
        codes = {item["code"] for item in validate_model(model)}
        self.assertIn("DUPLICATE_NODE_ID", codes)

    def test_unknown_node_reference_is_reported(self):
        model = json.loads(json.dumps(self.model))
        model["connections"][0]["source"]["node_id"] = "VEL-N-MISSING"
        codes = {item["code"] for item in validate_model(model)}
        self.assertIn("UNKNOWN_NODE", codes)

    def test_invalid_source_direction_is_reported(self):
        model = json.loads(json.dumps(self.model))
        model["connections"][0]["source"]["port_id"] = "request-in"
        codes = {item["code"] for item in validate_model(model)}
        self.assertIn("SOURCE_DIRECTION", codes)

    def test_channel_mismatch_is_reported(self):
        model = json.loads(json.dumps(self.model))
        model["connections"][0]["kind"] = "DATA"
        codes = {item["code"] for item in validate_model(model)}
        self.assertIn("CHANNEL_MISMATCH", codes)

    def test_unknown_group_member_is_reported(self):
        model = json.loads(json.dumps(self.model))
        model["groups"][0]["node_ids"].append("VEL-N-DOES-NOT-EXIST")
        codes = {item["code"] for item in validate_model(model)}
        self.assertIn("UNKNOWN_GROUP_MEMBER", codes)

    def test_dot_export_contains_nodes_and_edges(self):
        dot = to_dot(self.model)
        self.assertIn("digraph VEL", dot)
        self.assertIn("VEL-N-USER", dot)
        self.assertIn("VEL-C-USER-UI", dot)

    def test_canonical_json_is_deterministic(self):
        self.assertEqual(canonical_json(self.model), canonical_json(self.model))
        self.assertTrue(canonical_json(self.model).endswith("\n"))


if __name__ == "__main__":
    unittest.main()
