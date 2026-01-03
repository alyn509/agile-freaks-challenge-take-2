import requests
import json
import os

def get_live_location():
    IP_STACK_ACCESS_KEY = os.environ["IP_STACK_ACCESS_KEY"] 
    send_url = "http://api.ipstack.com/check?access_key={}".format(IP_STACK_ACCESS_KEY)
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    return [float(geo_json['latitude']), float(geo_json['longitude'])]
