import requests

class ISSHandler:
    def __init__(self, url):
        self.url = url

    def get_timestamps(self, latitude, longitude, number=5):
        url = self.url.format(lat=latitude, lon=longitude, n=number)
        resp = requests.get(url).json()['response']
        return resp
