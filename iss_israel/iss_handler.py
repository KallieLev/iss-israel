import requests

from iss_israel import cfg


class ISSHandler:
    def __init__(self):
        self.url = cfg['iss']['url']

    def get_timestamps(self, latitude, longitude, number=5):
        url = self.url.format(lat=latitude, lon=longitude, n=number)
        resp = requests.get(url).json()['response']
        return resp
