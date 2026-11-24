import unittest
from ves_forms import FormDefinition, FormField, validate_form_data


class FormValidationTests(unittest.TestCase):
    def test_accepts_valid_typed_form_data(self):
        form = FormDefinition("hardware.spec", [
            FormField("voltage", "Voltage", "number", required=True, minimum=0.1, maximum=24),
            FormField("interface", "Interface", "enum", required=True, choices=("I2C", "SPI")),
            FormField("enabled", "Enabled", "boolean", required=False),
        ])
        self.assertEqual(validate_form_data(form, {"voltage": 3.3, "interface": "I2C", "enabled": True}), [])

    def test_reports_missing_required_and_invalid_bounds(self):
        form = FormDefinition("hardware.spec", [
            FormField("voltage", "Voltage", "number", required=True, minimum=0, maximum=5),
            FormField("interface", "Interface", "enum", required=True, choices=("I2C", "SPI")),
            FormField("manufacturer", "Manufacturer", "text", required=True),
        ])
        errors = validate_form_data(form, {"voltage": 12, "interface": "CAN"})
        self.assertEqual({e.code for e in errors}, {"VES-FORM-REQUIRED", "VES-FORM-RANGE", "VES-FORM-CHOICE"})

    def test_rejects_boolean_as_number(self):
        form = FormDefinition("numeric", [FormField("count", "Count", "number")])
        errors = validate_form_data(form, {"count": True})
        self.assertIn("VES-FORM-TYPE", {e.code for e in errors})


if __name__ == "__main__":
    unittest.main()
