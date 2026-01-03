import unittest
import os
from helpers import run_finder

class TestSameLocationShops(unittest.TestCase):
    def test_same_location_shops(self):
        same_url = os.path.join(os.path.dirname(__file__), 'sets', 'same_location.csv')
        # Should work, with distance 0 for same location
        try:
            run_finder(same_url, 47.6, -122.4)
        except SystemExit:
            self.fail("Should not exit with same location shops")

if __name__ == "__main__":
    unittest.main()
