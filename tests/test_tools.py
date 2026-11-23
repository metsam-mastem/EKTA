import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import validate_docs
import build_graph

class EktaToolTests(unittest.TestCase):
    def test_documentation_validation(self):
        self.assertEqual(validate_docs.validate(), [])

    def test_graph_contains_concepts(self):
        graph = build_graph.build()
        self.assertGreaterEqual(len(graph["nodes"]), 7)
        ids = {node["id"] for node in graph["nodes"]}
        self.assertIn("EKTA-CON-000001", ids)
        self.assertIn("EKTA-CON-000003", ids)

if __name__ == "__main__":
    unittest.main()
