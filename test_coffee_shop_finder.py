import unittest
import pandas as pd
import os
from helpers.coffee_shop_finder import compute_closest_shops, find_and_print_closest_shops

class TestClosestShopsToLocation(unittest.TestCase):
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

    def test_malformed_data_invalid_coordinate(self):
        malformed_url = os.path.join(os.path.dirname(__file__), 'test_sets', 'malformed.csv')
        with self.assertRaises(SystemExit):
            find_and_print_closest_shops(malformed_url, 47.6, -122.4)

    def test_malformed_data_missing_coordinate(self):
        malformed_url = os.path.join(os.path.dirname(__file__), 'test_sets', 'malformed2.csv')
        with self.assertRaises(SystemExit):
            find_and_print_closest_shops(malformed_url, 47.6, -122.4)

    def test_empty_data(self):
        empty_url = os.path.join(os.path.dirname(__file__), 'test_sets', 'empty.csv')
        with self.assertRaises(SystemExit):
            find_and_print_closest_shops(empty_url, 47.6, -122.4)

    def test_one_shop(self):
        one_shop_url = os.path.join(os.path.dirname(__file__), 'test_sets', 'one_shop.csv')
        # Should work, but since it's print, hard to test output in unit test
        # For now, just ensure no exception
        try:
            find_and_print_closest_shops(one_shop_url, 47.6, -122.4)
        except SystemExit:
            self.fail("Should not exit with one valid shop")

    def test_invalid_y_coordinate(self):
        invalid_y_url = os.path.join(os.path.dirname(__file__), 'test_sets', 'invalid_y.csv')
        with self.assertRaises(SystemExit):
            find_and_print_closest_shops(invalid_y_url, 47.6, -122.4)

    def test_extra_columns(self):
        extra_url = os.path.join(os.path.dirname(__file__), 'test_sets', 'extra_columns.csv')
        # Should work, ignoring extra columns
        try:
            find_and_print_closest_shops(extra_url, 47.6, -122.4)
        except SystemExit:
            self.fail("Should not exit with extra columns")

    def test_same_location_shops(self):
        same_url = os.path.join(os.path.dirname(__file__), 'test_sets', 'same_location.csv')
        # Should work, with distance 0 for same location
        try:
            find_and_print_closest_shops(same_url, 47.6, -122.4)
        except SystemExit:
            self.fail("Should not exit with same location shops")

    def test_fewer_shops_than_requested(self):
        data = pd.DataFrame({
            'Name': ['Shop1'],
            'Y': [40.7128],
            'X': [-74.0060]
        })
        y, x = 39.9042, 116.4074
        result = compute_closest_shops(data, y, x, n=3)
        self.assertEqual(len(result), 1)  # Should return all available

    def test_distance_rounding(self):
        data = pd.DataFrame({
            'Name': ['Shop1'],
            'Y': [40.7128],
            'X': [-74.0060]
        })
        y, x = 40.7128, -74.0060  # Same location
        result = compute_closest_shops(data, y, x, n=1)
        self.assertAlmostEqual(result.iloc[0]['distance'], 0.0, places=4)
