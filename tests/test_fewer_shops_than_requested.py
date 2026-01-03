import unittest
import pandas as pd
from helpers.coffee_shop_finder import compute_closest_shops

class TestFewerShopsThanRequested(unittest.TestCase):
    def test_fewer_shops_than_requested(self):
        data = pd.DataFrame({
            'Name': ['Shop1'],
            'Y': [40.7128],
            'X': [-74.0060]
        })
        y, x = 39.9042, 116.4074
        result = compute_closest_shops(data, y, x, n=3)
        self.assertEqual(len(result), 1)  # Should return all available

if __name__ == "__main__":
    unittest.main()
