import argparse
import pandas as pd

from helpers.closest_shops_to_location import closest_shops_to_location

def main():
    parser = argparse.ArgumentParser(
        description="Find closest locations to given coordinates"
    )
    
    parser.add_argument("y", type=float, help="Y coordinate")
    parser.add_argument("x", type=float, help="X coordinate")
    parser.add_argument("url", type=str, help="Shop data url")

    args = parser.parse_args()

    data = pd.read_csv(args.url, names=['Name', 'Y', 'X'], dtype={'Name': str, 'Y': float, 'X': float})

    result = closest_shops_to_location(data, args.y, args.x)
    print(result[["Name", "distance"]].to_csv(index=False, header=False).strip())

if __name__ == "__main__":
    main()
