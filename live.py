import argparse

from helpers.live_location import get_live_location
from helpers import run_finder

def main():
    parser = argparse.ArgumentParser(
        description="Find closest coffee shops to your current location"
    )
    parser.add_argument("url", type=str, help="Shop data url")

    args = parser.parse_args()

    my_location = get_live_location()

    run_finder(args.url, my_location[0], my_location[1])
    
if __name__ == "__main__":
    main()
