import unittest
import os
from helpers import run_finder

class TestExtraColumns(unittest.TestCase):
    def test_extra_columns(self):
        extra_url = os.path.join(os.path.dirname(__file__), 'sets', 'extra_columns.csv')
        # Should work, ignoring extra columns
        try:
            run_finder(extra_url, 47.6, -122.4)
        except SystemExit:
            self.fail("Should not exit with extra columns")

if __name__ == "__main__":
    unittest.main()
