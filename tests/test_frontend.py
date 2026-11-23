import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_frontend import validate_frontend


class ExplorerFrontendTests(unittest.TestCase):
    def test_explorer_has_rtl_shell_and_valid_javascript(self):
        errors = validate_frontend(ROOT / "runtime" / "web" / "index.html", require_node=False)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
