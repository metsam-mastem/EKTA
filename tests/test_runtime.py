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
        cls.atlas = AtlasRepository(ROOT)

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

    def test_unified_search_and_facets_endpoints(self):
        result = self.client.get("/api/v1/search", params={"q": "#runtime"})
        self.assertEqual(result.status_code, 200)
        self.assertTrue(any(item["id"] == "EKTA-CON-000001" for item in result.json()["results"]))
        facets = self.client.get("/api/v1/facets")
        self.assertEqual(facets.status_code, 200)
        self.assertIn("tags", facets.json())

    def test_document_detail_endpoint_is_id_scoped(self):
        search = self.client.get("/api/v1/search", params={"q": "knowledge lifecycle kind:document"}).json()
        item = next(item for item in search["results"] if item["source_file"] == "docs/END_TO_END_LIFECYCLE.md")
        detail = self.client.get("/api/v1/documents/" + item["id"])
        self.assertEqual(detail.status_code, 200)
        self.assertIn("Traceability chain", detail.json()["content"])
        self.assertEqual(self.client.get("/api/v1/documents/EKTA-DOC-invalid").status_code, 404)

    def test_browser_explorer_is_served(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("EKTA", response.text)

    def test_hashtag_search_matches_concept_name_and_taxonomy(self):
        by_name = self.atlas.search("#runtime")
        self.assertTrue(any(item["id"] == "EKTA-CON-000001" for item in by_name["results"]))
        by_domain = self.atlas.search("#software-engineering")
        self.assertTrue(any(item["id"] == "EKTA-CON-000001" for item in by_domain["results"]))

    def test_fielded_query_filters_concepts(self):
        result = self.atlas.search("domain:software-engineering layer:platform-runtime")
        self.assertTrue(result["results"])
        self.assertTrue(all("software-engineering" in item.get("domains", []) for item in result["results"]))

    def test_search_returns_explainable_match_metadata(self):
        result = self.atlas.search("runtime")
        item = next(item for item in result["results"] if item["id"] == "EKTA-CON-000001")
        self.assertGreater(item["score"], 0)
        self.assertTrue(item["matched_fields"])
        self.assertTrue(item["snippet"])

    def test_repository_document_search_and_safe_detail(self):
        result = self.atlas.search("knowledge lifecycle kind:document")
        self.assertTrue(any(item["source_file"] == "docs/END_TO_END_LIFECYCLE.md" for item in result["results"]))
        document = next(item for item in result["results"] if item["source_file"] == "docs/END_TO_END_LIFECYCLE.md")
        detail = self.atlas.get_document(document["id"])
        self.assertIn("Traceability chain", detail["content"])
        self.assertIsNone(self.atlas.get_document("EKTA-DOC-not-a-valid-id"))

    def test_search_supports_status_and_kind_filters(self):
        result = self.atlas.search("runtime status:PROPOSED kind:concept")
        self.assertTrue(result["results"])
        self.assertTrue(all(item["kind"] == "concept" and item["status"] == "PROPOSED" for item in result["results"]))

    def test_facets_include_tags_and_taxonomy_values(self):
        facets = self.atlas.facets()
        self.assertIn("software-engineering", [item["id"] for item in facets["domains"]])
        self.assertIn("runtime", facets["tags"])


if __name__ == "__main__":
    unittest.main()
