import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))

from ekta_runtime.repository import AtlasRepository


class RuntimeRepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = AtlasRepository(ROOT)

    def test_runtime_loads_canonical_concepts(self):
        self.assertGreaterEqual(len(self.atlas.records), 7)
        self.assertIn("EKTA-CON-000001", self.atlas.by_id)

    def test_concept_lookup_returns_canonical_record(self):
        record = self.atlas.get_concept("EKTA-CON-000001")
        self.assertEqual(record["canonical_name"], "Runtime")
        self.assertIn("body", record)

    def test_unknown_concept_returns_none(self):
        self.assertIsNone(self.atlas.get_concept("EKTA-CON-999999"))

    def test_search_matches_alias_and_definition(self):
        results = self.atlas.list_concepts(query="execution environment")
        self.assertTrue(any(item["id"] == "EKTA-CON-000001" for item in results))

    def test_taxonomy_is_exposed(self):
        taxonomy = self.atlas.taxonomy()
        self.assertGreaterEqual(len(taxonomy["domains"]["domains"]), 20)
        self.assertIn("DEPENDS_ON", taxonomy["relations"])

    def test_graph_contains_typed_edges_and_resolution_state(self):
        graph = self.atlas.graph_data
        self.assertGreaterEqual(graph["summary"]["node_count"], 7)
        self.assertGreater(graph["summary"]["edge_count"], 0)
        self.assertTrue(any(edge["predicate"] == "IS_A" for edge in graph["edges"]))
        self.assertTrue(any(edge["status"] != "resolved" for edge in graph["edges"]))

    def test_invalid_predicates_are_not_silently_accepted(self):
        graph = self.atlas.graph_data
        self.assertTrue(any(edge["status"] == "invalid_predicate" for edge in graph["edges"]))


if __name__ == "__main__":
    unittest.main()
