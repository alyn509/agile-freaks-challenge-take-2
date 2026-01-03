import unittest
import os
from helpers.coffee_shop_finder import find_and_print_closest_shops

class TestInvalidYCoordinate(unittest.TestCase):
    def test_invalid_y_coordinate(self):
        invalid_y_url = os.path.join(os.path.dirname(__file__), 'sets', 'invalid_y.csv')
        with self.assertRaises(SystemExit):
            find_and_print_closest_shops(invalid_y_url, 47.6, -122.4)

if __name__ == "__main__":
    unittest.main()
