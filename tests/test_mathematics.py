import unittest

from ekta_runtime.mathematics import (
    validate_coordinate_frame,
    validate_mathematical_object,
    validate_relation_graph,
)


def quadratic():
    return {
        "schema_version": "0.1.0",
        "id": "UMO-FUNCTION-QUADRATIC-001",
        "kind": "function",
        "status": "PROPOSED",
        "identity": {"canonical_name": "Quadratic function", "aliases": ["تابع درجه دوم"]},
        "revision": "0.1.0",
        "semantics": {"definition": "A polynomial function of degree exactly two."},
        "structure": {"dimensions": 1, "domain": "real", "codomain": "real"},
        "behavior": {"operations": [{"name": "evaluate"}]},
        "relations": [{"predicate": "IS_A", "target_id": "UMO-FUNCTION-POLYNOMIAL-001"}],
        "representations": [{"representation_type": "symbolic", "payload": "f(x)=ax^2+bx+c"}],
    }


class MathematicalObjectTests(unittest.TestCase):
    def test_valid_object_passes(self):
        self.assertEqual(validate_mathematical_object(quadratic()), [])

    def test_short_definition_is_rejected(self):
        record = quadratic()
        record["semantics"] = {"definition": "short"}
        self.assertTrue(validate_mathematical_object(record))

    def test_unknown_representation_is_rejected(self):
        record = quadratic()
        record["representations"] = [{"representation_type": "hologram"}]
        self.assertTrue(validate_mathematical_object(record))

    def test_coordinate_frame_passes(self):
        frame = {"id": "FRAME-XY", "dimension": 2, "axes": [{"id": "x", "label": "X"}, {"id": "y", "label": "Y"}], "origin": [0, 0]}
        self.assertEqual(validate_coordinate_frame(frame), [])

    def test_coordinate_origin_dimension_is_checked(self):
        frame = {"id": "FRAME-XY", "dimension": 2, "axes": [{"id": "x", "label": "X"}, {"id": "y", "label": "Y"}], "origin": [0]}
        self.assertIn("origin length must equal dimension", validate_coordinate_frame(frame))

    def test_relation_target_must_exist(self):
        self.assertTrue(validate_relation_graph([quadratic()]))

    def test_closed_relation_graph_passes(self):
        first = quadratic()
        second = {"id": "UMO-FUNCTION-POLYNOMIAL-001", "relations": []}
        self.assertEqual(validate_relation_graph([first, second]), [])


class MathematicalSchemaTests(unittest.TestCase):
    def test_umo_schema_is_valid_and_example_conforms(self):
        import json
        from pathlib import Path
        import jsonschema

        root = Path(__file__).resolve().parents[1]
        schema = json.loads((root / "schemas" / "mathematical-object.schema.json").read_text(encoding="utf-8"))
        instance = json.loads((root / "examples" / "mathematical-universe" / "quadratic-function.umo.json").read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
        validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
        self.assertEqual(list(validator.iter_errors(instance)), [])

    def test_coordinate_frame_schema_is_valid(self):
        import json
        from pathlib import Path
        import jsonschema

        root = Path(__file__).resolve().parents[1]
        schema = json.loads((root / "schemas" / "coordinate-frame.schema.json").read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)


if __name__ == "__main__":
    unittest.main()
