import json
import unittest
from dataclasses import asdict
from pathlib import Path
from jsonschema import Draft202012Validator
from ves_core import Project, VesService


class SchemaContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.schemas = {p.name.removesuffix(".schema.json"): json.loads(p.read_text(encoding="utf-8")) for p in (cls.root / "schemas").glob("*.schema.json")}

    def test_all_schema_documents_are_valid_json_schemas(self):
        for schema in self.schemas.values():
            Draft202012Validator.check_schema(schema)

    def test_project_and_nested_records_validate(self):
        project = Project.create("Schema Fixture")
        service = VesService(project)
        source = service.add_entity("hardware.mcu", "MCU")
        target = service.add_entity("hardware.sensor", "Sensor")
        service.add_relationship(source.id, target.id, "connects_to")
        board = service.add_board("Architecture")
        service.place_entity(board.id, source.id, 10, 20)
        Draft202012Validator(self.schemas["project"]).validate(project.to_dict())
        Draft202012Validator(self.schemas["entity"]).validate(asdict(source))
        Draft202012Validator(self.schemas["relationship"]).validate(asdict(next(iter(project.relationships.values()))))
        Draft202012Validator(self.schemas["board"]).validate({"id": board.id, "name": board.name, "board_type": board.board_type, "placements": [asdict(p) for p in board.placements]})


if __name__ == "__main__":
    unittest.main()
