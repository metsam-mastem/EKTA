import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "projects/ecps/src"))

from ecps.contracts import validate_manifest, compile_projection_plan


class ProjectionContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((ROOT / "projects/ecps/examples/integrated-engineering-view.json").read_text())

    def test_reference_manifest_is_valid(self):
        self.assertEqual(validate_manifest(self.manifest), [])

    def test_duplicate_source_ids_are_rejected(self):
        data = json.loads(json.dumps(self.manifest))
        data["sourceModels"].append(json.loads(json.dumps(data["sourceModels"][0])))
        codes = {item["code"] for item in validate_manifest(data)}
        self.assertIn("DUPLICATE_SOURCE_MODEL_ID", codes)

    def test_projection_must_reference_existing_source(self):
        data = json.loads(json.dumps(self.manifest))
        data["projections"][0]["sourceModelRef"] = "src.missing"
        codes = {item["code"] for item in validate_manifest(data)}
        self.assertIn("UNKNOWN_SOURCE_MODEL", codes)

    def test_projection_must_reference_existing_coordinate_space(self):
        data = json.loads(json.dumps(self.manifest))
        data["projections"][0]["coordinateSpaceRef"] = "space.missing"
        codes = {item["code"] for item in validate_manifest(data)}
        self.assertIn("UNKNOWN_COORDINATE_SPACE", codes)

    def test_board_layout_cannot_be_used_as_physical_geometry(self):
        data = json.loads(json.dumps(self.manifest))
        data["projections"][1]["coordinateSpaceRef"] = "space.board"
        codes = {item["code"] for item in validate_manifest(data)}
        self.assertIn("COORDINATE_KIND_MISMATCH", codes)

    def test_semantic_address_cannot_be_used_as_cartesian_geometry(self):
        data = json.loads(json.dumps(self.manifest))
        data["projections"][1]["coordinateSpaceRef"] = "space.semantic"
        codes = {item["code"] for item in validate_manifest(data)}
        self.assertIn("COORDINATE_KIND_MISMATCH", codes)

    def test_coordinate_space_authority_must_match_projection_source(self):
        data = json.loads(json.dumps(self.manifest))
        data["coordinateSpaces"][0]["authority"] = "MUA"
        codes = {item["code"] for item in validate_manifest(data)}
        self.assertIn("AUTHORITY_SOURCE_MISMATCH", codes)

    def test_projection_plan_is_deterministic_and_read_only(self):
        first = compile_projection_plan(self.manifest, "view.semantic")
        second = compile_projection_plan(self.manifest, "view.semantic")
        self.assertEqual(first, second)
        self.assertTrue(first["readOnly"])
        self.assertEqual(first["coordinateKind"], "semantic-address")

    def test_unknown_projection_id_raises(self):
        with self.assertRaises(KeyError):
            compile_projection_plan(self.manifest, "view.unknown")

    def test_manifest_matches_json_schema(self):
        import jsonschema
        schema = json.loads((ROOT / "schemas/ecps-projection.schema.json").read_text())
        jsonschema.Draft202012Validator.check_schema(schema)
        errors = list(jsonschema.Draft202012Validator(schema).iter_errors(self.manifest))
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
