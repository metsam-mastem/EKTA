import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))

from fastapi.testclient import TestClient
from ekta_runtime.repository import AtlasRepository
from ekta_runtime.api import app


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


class RuntimeApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

    def test_concept_list_and_detail_endpoints(self):
        listing = self.client.get("/api/v1/concepts")
        self.assertEqual(listing.status_code, 200)
        self.assertGreaterEqual(listing.json()["count"], 7)
        detail = self.client.get("/api/v1/concepts/EKTA-CON-000001")
        self.assertEqual(detail.status_code, 200)
        self.assertEqual(detail.json()["canonical_name"], "Runtime")

    def test_unknown_concept_returns_http_404(self):
        response = self.client.get("/api/v1/concepts/EKTA-CON-999999")
        self.assertEqual(response.status_code, 404)

    def test_overview_taxonomy_and_graph_endpoints(self):
        self.assertEqual(self.client.get("/api/v1/overview").status_code, 200)
        self.assertEqual(self.client.get("/api/v1/taxonomy").status_code, 200)
        graph = self.client.get("/api/v1/graph")
        self.assertEqual(graph.status_code, 200)
        self.assertGreater(graph.json()["summary"]["edge_count"], 0)

    def test_browser_explorer_is_served(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("EKTA", response.text)


if __name__ == "__main__":
    unittest.main()
