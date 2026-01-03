import unittest
import os
from helpers.coffee_shop_finder import find_and_print_closest_shops

class TestMalformedDataInvalidCoordinate(unittest.TestCase):
    def test_malformed_data_invalid_coordinate(self):
        malformed_url = os.path.join(os.path.dirname(__file__), 'sets', 'malformed.csv')
        with self.assertRaises(SystemExit):
            find_and_print_closest_shops(malformed_url, 47.6, -122.4)

if __name__ == "__main__":
    unittest.main()
