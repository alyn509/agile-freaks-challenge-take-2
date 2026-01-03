import unittest
import os
from helpers import run_finder

class TestOneShop(unittest.TestCase):
    def test_one_shop(self):
        one_shop_url = os.path.join(os.path.dirname(__file__), 'sets', 'one_shop.csv')
        # Should work, but since it's print, hard to test output in unit test
        # For now, just ensure no exception
        try:
            run_finder(one_shop_url, 47.6, -122.4)
        except SystemExit:
            self.fail("Should not exit with one valid shop")

if __name__ == "__main__":
    unittest.main()
