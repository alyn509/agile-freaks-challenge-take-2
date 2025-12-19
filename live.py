import argparse
import pandas as pd

from helpers.get_live_location import get_live_location
from helpers.closest_shops_to_location import closest_shops_to_location

def main():
    parser = argparse.ArgumentParser(
        description="Find closest locations to given coordinates"
    )
    parser.add_argument("url", type=str, help="Shop data url")

    args = parser.parse_args()

    my_location = get_live_location()

    data = pd.read_csv(args.url, names=['Name', 'Y', 'X'], dtype={'Name': str, 'Y': float, 'X': float})

    result = closest_shops_to_location(data, my_location[0], my_location[1])
    print(result[["Name", "distance"]].to_csv(index=False, header=False).strip())

if __name__ == "__main__":
    main()
