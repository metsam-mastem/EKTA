"""Unit tests for the UMSF semantic coordinate and graph validator."""
import json
import unittest
from pathlib import Path

import jsonschema

from ekta_runtime.umsf import (
    Entity,
    Relationship,
    SemanticAddress,
    SystemModel,
    model_from_dict,
    model_to_dict,
    validate_model,
)


class UMSFValidationTests(unittest.TestCase):
    def setUp(self):
        self.address = SemanticAddress(
            x_layer_id="application-agent",
            y_module_id="module.identity",
            z_depth=1,
            valid_from="2026-01-01T00:00:00Z",
        )
        self.root = Entity("system.root", "system", "Example System")
        self.module = Entity("module.identity", "module", "Identity Module", (self.address,))
        self.model = SystemModel(
            "model.example",
            "system.root",
            "view.system-context",
            (self.root, self.module),
            (Relationship("module.identity", "PART_OF", "system.root"),),
        )

    def test_accepts_valid_model_with_known_registries(self):
        self.assertEqual(
            validate_model(self.model, {"application-agent"}, {"PART_OF"}),
            [],
        )

    def test_accepts_generator_registries_across_multiple_addresses(self):
        second = SemanticAddress(
            "application-agent", "module.identity", 2, "2026-01-01T00:00:00Z"
        )
        model = SystemModel(
            "model.example", "system.root", "view.system-context",
            (self.root, Entity("module.identity", "module", "Identity Module", (self.address, second))),
        )
        self.assertEqual(
            validate_model(model, (item for item in ["application-agent"])),
            [],
        )

    def test_rejects_negative_depth(self):
        bad = SemanticAddress("application-agent", "module.identity", -1, "2026-01-01T00:00:00Z")
        self.assertIn("z_depth must be a non-negative integer", bad.validate())

    def test_rejects_boolean_depth_even_though_bool_is_an_int_subclass(self):
        bad = SemanticAddress("application-agent", "module.identity", True, "2026-01-01T00:00:00Z")
        self.assertIn("z_depth must be a non-negative integer", bad.validate())

    def test_requires_timezone_aware_timestamp(self):
        bad = SemanticAddress("application-agent", "module.identity", 0, "2026-01-01T00:00:00")
        self.assertIn("valid_from must include a timezone offset", bad.validate())

    def test_rejects_reversed_validity_interval(self):
        bad = SemanticAddress(
            "application-agent",
            "module.identity",
            0,
            "2026-02-01T00:00:00Z",
            "2026-01-01T00:00:00Z",
        )
        self.assertIn("valid_to must be later than valid_from", bad.validate())

    def test_rejects_unknown_layer(self):
        errors = validate_model(self.model, {"platform-runtime"}, {"PART_OF"})
        self.assertTrue(any("unknown layer id: application-agent" in item for item in errors))

    def test_rejects_missing_relationship_endpoint_and_predicate(self):
        broken = SystemModel(
            "model.example",
            "system.root",
            "view.system-context",
            (self.root,),
            (Relationship("missing", "MADE_UP", "also-missing"),),
        )
        errors = validate_model(broken, {"application-agent"}, {"PART_OF"})
        self.assertTrue(any("source not found: missing" in item for item in errors))
        self.assertTrue(any("target not found: also-missing" in item for item in errors))
        self.assertTrue(any("unknown predicate: MADE_UP" in item for item in errors))

    def test_rejects_duplicate_entity_ids(self):
        duplicate = SystemModel(
            "model.example",
            "system.root",
            "view.system-context",
            (self.root, self.root),
        )
        self.assertTrue(any("duplicate entity id: system.root" in item for item in validate_model(duplicate)))

    def test_serializes_without_changing_identity(self):
        data = model_to_dict(self.model)
        self.assertEqual(data["entities"][1]["id"], "module.identity")
        self.assertEqual(data["entities"][1]["addresses"][0]["z_depth"], 1)
        self.assertEqual(data["schema_version"], "0.1.0")

    def test_round_trip_preserves_identity_relationships_and_provenance(self):
        source = SystemModel(
            "model.example", "system.root", "view.system-context",
            (self.root, self.module),
            (Relationship("module.identity", "PART_OF", "system.root", "architecture", "VERIFIED"),),
            ({"source_id": "EKTA-SRC-000001", "retrieved_at": "2026-11-24"},),
        )
        restored = model_from_dict(model_to_dict(source))
        self.assertEqual(model_to_dict(restored), model_to_dict(source))
        self.assertEqual(validate_model(restored, {"application-agent"}, {"PART_OF"}), [])

    def test_import_rejects_unsupported_schema_version(self):
        with self.assertRaisesRegex(ValueError, "unsupported UMSF schema_version"):
            model_from_dict({"schema_version": "9.9.9"})

    def test_import_rejects_malformed_nested_entity(self):
        payload = model_to_dict(self.model)
        payload["entities"][1]["addresses"] = [{"x_layer_id": "x"}]
        with self.assertRaisesRegex(ValueError, "missing y_module_id"):
            model_from_dict(payload)

    def test_validator_reports_malformed_runtime_objects_without_crashing(self):
        malformed = SystemModel(
            "model.example", "system.root", "view.system-context",
            (Entity(None, None, None),),  # type: ignore[arg-type]
        )
        errors = validate_model(malformed)
        self.assertTrue(any("id must be non-empty" in item for item in errors))
        self.assertTrue(any("type must be non-empty" in item for item in errors))
        self.assertTrue(any("name must be non-empty" in item for item in errors))

    def test_serialized_model_matches_json_schema(self):
        schema_path = Path(__file__).resolve().parents[1] / "schemas" / "umsf.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.validate(model_to_dict(self.model), schema, format_checker=jsonschema.FormatChecker())


if __name__ == "__main__":
    unittest.main()
