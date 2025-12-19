import argparse
import pandas as pd
import numpy as np
import requests
import json

from constants import IP_STACK_ACCESS_KEY

def closest_shops_to_location(data, y, x, n=3):
    distance = np.sqrt((data["Y"] - y) ** 2 + (data["X"] - x) ** 2)
    data["distance"] = np.round(distance, 4)

    return data.sort_values(by="distance", ascending=True).head(n)

def get_live_location():
    send_url = "http://api.ipstack.com/check?access_key={}".format(IP_STACK_ACCESS_KEY)
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    return [float(geo_json['latitude']), float(geo_json['longitude'])]

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
