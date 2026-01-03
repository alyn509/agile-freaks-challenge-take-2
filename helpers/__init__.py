import argparse
from helpers.coffee_shop_finder import find_and_print_closest_shops

def run_finder(url, y, x):
    find_and_print_closest_shops(url, y, x)
