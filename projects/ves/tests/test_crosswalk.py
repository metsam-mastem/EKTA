import json
import unittest
from pathlib import Path
import yaml


class EktaCrosswalkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[3]
        cls.crosswalk = json.loads((Path(__file__).resolve().parents[1] / "integration" / "ekta-taxonomy-crosswalk.json").read_text(encoding="utf-8"))

    def test_all_crosswalk_ids_exist_in_canonical_registries(self):
        taxonomy = self.root / "taxonomy"
        territories = {x["id"] for x in yaml.safe_load((taxonomy / "territories.yml").read_text(encoding="utf-8"))["territories"]}
        domains = {x["id"] for x in yaml.safe_load((taxonomy / "domains.yml").read_text(encoding="utf-8"))["domains"]}
        layers = {x["id"] for x in yaml.safe_load((taxonomy / "layers.yml").read_text(encoding="utf-8"))["layers"]}
        knowledge_types = set(yaml.safe_load((taxonomy / "knowledge-types.yml").read_text(encoding="utf-8"))["knowledge_types"])
        relations = set(yaml.safe_load((taxonomy / "relations.yml").read_text(encoding="utf-8"))["relations"])
        self.assertTrue(set(self.crosswalk["territory_ids"]).issubset(territories))
        self.assertTrue(set(self.crosswalk["domain_ids"]).issubset(domains))
        self.assertTrue(set(self.crosswalk["layer_ids"]).issubset(layers))
        self.assertTrue(set(self.crosswalk["knowledge_type_ids"]).issubset(knowledge_types))
        for item in self.crosswalk["relation_mappings"]:
            if item["ekta"] is not None:
                self.assertIn(item["ekta"], relations)

    def test_no_relation_is_mapped_as_exact_when_it_is_approximate_or_inverse(self):
        for item in self.crosswalk["relation_mappings"]:
            if item["mapping"] in {"inverse", "approximate", "no-direct-equivalent"}:
                self.assertNotEqual(item["mapping"], "direct")


if __name__ == "__main__":
    unittest.main()
