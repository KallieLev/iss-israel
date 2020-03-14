import json
import requests

with open('../config.json', 'r') as config_file:
    cfg = json.load(config_file)


class ISSHandler:
    def __init__(self):
        self.url = cfg['iss']['url']

    def get_timestamps(self, latitude, longitude, number=5):
        url = self.url.format(lat=latitude, lon=longitude, n=number)
        resp = requests.get(url).json()['response']
        return resp
