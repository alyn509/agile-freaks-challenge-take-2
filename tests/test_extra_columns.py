import unittest
import os
from helpers.coffee_shop_finder import find_and_print_closest_shops

class TestExtraColumns(unittest.TestCase):
    def test_extra_columns(self):
        extra_url = os.path.join(os.path.dirname(__file__), 'sets', 'extra_columns.csv')
        # Should work, ignoring extra columns
        try:
            find_and_print_closest_shops(extra_url, 47.6, -122.4)
        except SystemExit:
            self.fail("Should not exit with extra columns")

if __name__ == "__main__":
    unittest.main()
