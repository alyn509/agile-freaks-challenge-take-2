import unittest
import pandas as pd
from helpers.coffee_shop_finder import compute_closest_shops

class TestClosestShops(unittest.TestCase):
    def test_closest_shops(self):
        data = pd.DataFrame({
            'Name': ['Shop1', 'Shop2', 'Shop3', 'Shop4'],
            'Y': [40.7128, 34.0522, 41.8781, 29.7604],
            'X': [-74.0060, -118.2437, -87.6298, -95.3698]
        })
        y, x = 39.9042, 116.4074
        result = compute_closest_shops(data, y, x, n=2)
        self.assertEqual(len(result), 2)
        self.assertIn('distance', result.columns)
        self.assertLessEqual(result.iloc[0]['distance'], result.iloc[1]['distance'])

if __name__ == "__main__":
    unittest.main()
