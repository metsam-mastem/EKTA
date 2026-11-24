import json
import sys
import unittest
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_usdo import validate


class USDOSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads((ROOT / "schemas" / "usdo-entity.schema.json").read_text(encoding="utf-8"))
        cls.validator = jsonschema.Draft202012Validator(cls.schema)
        cls.example = yaml.safe_load((ROOT / "examples" / "USDO_CPU_EXAMPLE.yml").read_text(encoding="utf-8"))

    def test_schema_is_valid(self):
        jsonschema.Draft202012Validator.check_schema(self.schema)

    def test_cpu_example_matches_schema(self):
        self.assertEqual(list(self.validator.iter_errors(self.example)), [])

    def test_all_twelve_facets_are_required(self):
        candidate = dict(self.example)
        candidate["facets"] = {"ontology": {}}
        self.assertTrue(list(self.validator.iter_errors(candidate)))

    def test_macro_meso_micro_is_not_a_scale_field(self):
        candidate = dict(self.example)
        candidate["abstraction_level"] = "nano"
        self.assertTrue(list(self.validator.iter_errors(candidate)))

    def test_circuit_kind_is_domain_qualified(self):
        candidate = json.loads(json.dumps(self.example))
        candidate["facets"]["circuits"][0]["kind"] = "graph_cycle"
        self.assertTrue(list(self.validator.iter_errors(candidate)))

    def test_relation_requires_predicate_and_target(self):
        candidate = json.loads(json.dumps(self.example))
        candidate["facets"]["relations"] = [{"predicate": "PART_OF"}]
        self.assertTrue(list(self.validator.iter_errors(candidate)))

    def test_repository_validator_passes(self):
        self.assertEqual(validate(), [])


if __name__ == "__main__":
    unittest.main()
