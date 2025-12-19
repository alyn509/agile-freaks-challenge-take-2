import numpy as np
import math

def closest_shops_to_location(data, y, x, n=3):

    res = []
    for data_row in data.itertuples(index=False):
        # Using haversine formula to calculate distance between two latitude / longitude points
        distance = haversine(data_row.Y, data_row.X, y, x)
        res.append(np.round(distance, 4))

    data["distance"] = res
    return data.sort_values(by="distance", ascending=True).head(n)

def haversine(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of Earth in kilometers
    r = 6371
    return c * r
