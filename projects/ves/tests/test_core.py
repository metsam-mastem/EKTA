import unittest
from ves_core import Project, VesService, Relationship


class VesCoreTests(unittest.TestCase):
    def setUp(self):
        self.project = Project.create("Embedded Controller")
        self.service = VesService(self.project)

    def test_create_entity_and_preserve_properties(self):
        entity = self.service.add_entity("hardware.mcu", "MCU", {"voltage_v": 3.3}, ["compute"])
        self.assertEqual(entity.properties["voltage_v"], 3.3)
        self.assertIn(entity.id, self.project.entities)

    def test_relationship_requires_existing_endpoints(self):
        entity = self.service.add_entity("hardware.mcu", "MCU")
        with self.assertRaises(KeyError):
            self.service.add_relationship(entity.id, "missing", "connects_to")

    def test_board_placement_rejects_duplicate(self):
        entity = self.service.add_entity("hardware.sensor", "Sensor")
        board = self.service.add_board("System Board")
        self.service.place_entity(board.id, entity.id, 12, 24)
        with self.assertRaises(ValueError):
            self.service.place_entity(board.id, entity.id)

    def test_round_trip_preserves_ids_relationships_and_placements(self):
        mcu = self.service.add_entity("hardware.mcu", "MCU", {"cores": 2})
        sensor = self.service.add_entity("hardware.sensor", "Sensor")
        self.service.add_relationship(mcu.id, sensor.id, "communicates_with", {"protocol": "I2C"})
        board = self.service.add_board("Architecture")
        self.service.place_entity(board.id, mcu.id, 10, 20)
        self.service.place_entity(board.id, sensor.id, 30, 40)
        restored = VesService.import_data(self.service.export())
        self.assertEqual(set(restored.project.entities), set(self.project.entities))
        self.assertEqual(len(restored.project.relationships), 1)
        rb = next(iter(restored.project.boards.values()))
        self.assertEqual([(p.x, p.y) for p in rb.placements], [(10.0, 20.0), (30.0, 40.0)])

    def test_validator_detects_dangling_relationship(self):
        self.project.relationships["rel_broken"] = Relationship("rel_broken", "missing-a", "missing-b", "depends_on")
        codes = {f.code for f in self.service.validate()}
        self.assertIn("VES-REL-001", codes)
        self.assertIn("VES-REL-002", codes)

    def test_rejects_empty_names_and_unknown_schema(self):
        with self.assertRaises(ValueError):
            Project.create("   ")
        with self.assertRaises(ValueError):
            self.service.add_entity("hardware.mcu", "   ")
        with self.assertRaises(ValueError):
            Project.from_dict({"schema_version": "9.0.0"})


if __name__ == "__main__":
    unittest.main()
