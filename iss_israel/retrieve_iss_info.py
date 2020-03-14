from iss_israel.iss_handler import ISSHandler
from dal.postgre_dal import PostgreDal
from iss_israel.timestamp_helper import convert_timezone
import json

with open('../config.json', 'r') as config_file:
    cfg = json.load(config_file)


class RetrieveISSInfo:
    def __init__(self):
        self.iss_handler = ISSHandler()
        self.postgre_dal = PostgreDal()

    def get_cities_info(self):
        cities_info = {}
        cities = cfg['iss']['cities']
        for city in cities.keys():
            info = self.iss_handler.get_timestamps(cities[city]['latitude'], cities[city]['longitude'],
                                                   cfg['iss']['number_of_events'])
            cities_info[city] = info
        return cities_info

    def insert_cities_info_postgre(self):
        cities_info = self.get_cities_info()
        for city, info in cities_info.items():
            for event in info:
                rise_time = convert_timezone(event['risetime'], cfg['iss']['from_timezone'], cfg['iss']['to_timezone'])
                self.postgre_dal.insert_city(city, event['duration'], rise_time)

        self.postgre_dal.commit()

if __name__ == '__main__':
    retrieve_info = RetrieveISSInfo()
    retrieve_info.insert_cities_info_postgre()