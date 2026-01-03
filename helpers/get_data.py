
import pandas as pd
import sys

def get_data_from_url(url):
    try:
        data = pd.read_csv(url, names=['Name', 'Y', 'X'], dtype={'Name': str, 'Y': float, 'X': float}, usecols=[0,1,2])
    except Exception as e:
        print(f"Error reading data from URL: {e}", file=sys.stderr)
        sys.exit(1)
    
    if data.empty:
        print("No coffee shop data found", file=sys.stderr)
        sys.exit(1)
    
    if data[['Y', 'X']].isnull().any().any():
        print("Malformed entries found in coffee shop data: missing or invalid coordinates", file=sys.stderr)
        sys.exit(1)
    
    return data
