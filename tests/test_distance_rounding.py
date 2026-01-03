import unittest
import pandas as pd
from helpers.coffee_shop_finder import compute_closest_shops

class TestDistanceRounding(unittest.TestCase):
    def test_distance_rounding(self):
        data = pd.DataFrame({
            'Name': ['Shop1'],
            'Y': [40.7128],
            'X': [-74.0060]
        })
        y, x = 40.7128, -74.0060  # Same location
        result = compute_closest_shops(data, y, x, n=1)
        self.assertAlmostEqual(result.iloc[0]['distance'], 0.0, places=4)

if __name__ == "__main__":
    unittest.main()
