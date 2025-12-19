import requests
import json

from helpers.constants import IP_STACK_ACCESS_KEY

def get_live_location():
    send_url = "http://api.ipstack.com/check?access_key={}".format(IP_STACK_ACCESS_KEY)
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    return [float(geo_json['latitude']), float(geo_json['longitude'])]
