import numpy as np

def closest_shops_to_location(data, y, x, n=3):
    distance = np.sqrt((data["Y"] - y) ** 2 + (data["X"] - x) ** 2)
    data["distance"] = np.round(distance, 4)

    return data.sort_values(by="distance", ascending=True).head(n)
