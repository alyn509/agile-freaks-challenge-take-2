import unittest
import os
from helpers.coffee_shop_finder import find_and_print_closest_shops

class TestEmptyData(unittest.TestCase):
    def test_empty_data(self):
        empty_url = os.path.join(os.path.dirname(__file__), 'sets', 'empty.csv')
        with self.assertRaises(SystemExit):
            find_and_print_closest_shops(empty_url, 47.6, -122.4)

if __name__ == "__main__":
    unittest.main()
