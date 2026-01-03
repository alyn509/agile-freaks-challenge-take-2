import unittest
import os
from helpers import run_finder

class TestEmptyData(unittest.TestCase):
    def test_empty_data(self):
        empty_url = os.path.join(os.path.dirname(__file__), 'sets', 'empty.csv')
        with self.assertRaises(SystemExit):
            run_finder(empty_url, 47.6, -122.4)

if __name__ == "__main__":
    unittest.main()
