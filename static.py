import argparse

from helpers import run_finder

def main():
    parser = argparse.ArgumentParser(
        description="Find closest coffee shops to given coordinates"
    )
    
    parser.add_argument("y", type=float, help="Y coordinate")
    parser.add_argument("x", type=float, help="X coordinate")
    parser.add_argument("url", type=str, help="Shop data url")

    args = parser.parse_args()

    run_finder(args.url, args.y, args.x)
    
if __name__ == "__main__":
    main()
