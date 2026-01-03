import unittest
import os
from helpers import run_finder

class TestMalformedDataMissingCoordinate(unittest.TestCase):
    def test_malformed_data_missing_coordinate(self):
        malformed_url = os.path.join(os.path.dirname(__file__), 'sets', 'malformed2.csv')
        with self.assertRaises(SystemExit):
            run_finder(malformed_url, 47.6, -122.4)

if __name__ == "__main__":
    unittest.main()
