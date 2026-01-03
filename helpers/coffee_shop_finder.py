import numpy as np
from geopy.distance import geodesic
from helpers.get_data import get_data_from_url

def compute_closest_shops(data, y, x, n=3):
    res = []
    for data_row in data.itertuples(index=False):
        distance = geodesic((data_row.Y, data_row.X), (y, x)).km
        res.append(np.round(distance, 4))

    data["distance"] = res
    return data.sort_values(by="distance", ascending=True).head(n)

def find_and_print_closest_shops(url, y, x):
    data = get_data_from_url(url)  
    
    result = compute_closest_shops(data, y, x)
    print(result[["Name", "distance"]].to_csv(index=False, header=False).strip())
