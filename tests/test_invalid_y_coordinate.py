import unittest
import os
from helpers import run_finder

class TestInvalidYCoordinate(unittest.TestCase):
    def test_invalid_y_coordinate(self):
        invalid_y_url = os.path.join(os.path.dirname(__file__), 'sets', 'invalid_y.csv')
        with self.assertRaises(SystemExit):
            run_finder(invalid_y_url, 47.6, -122.4)

if __name__ == "__main__":
    unittest.main()
