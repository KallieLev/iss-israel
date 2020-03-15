from utils.timestamp_helper import convert_timezone


class RetrieveISSInfo:
    def __init__(self, api_handler, dal, cfg):
        self.api_handler = api_handler
        self.dal = dal
        self.cfg = cfg

    def get_cities_info(self):
        cities_info = {}
        cities = self.cfg['iss']['cities']
        for city in cities.keys():
            info = self.api_handler.get_timestamps(cities[city]['latitude'], cities[city]['longitude'],
                                                   self.cfg['iss']['number_of_events'])
            cities_info[city] = info
        return cities_info

    def save_cities_info(self):
        cities_info = self.get_cities_info()
        for city, info in cities_info.items():
            for event in info:
                rise_time = convert_timezone(event['risetime'], self.cfg['iss']['from_timezone'],
                                             self.cfg['iss']['to_timezone'])
                self.dal.insert_city(city, event['duration'], rise_time, self.cfg['table_name'])

        self.dal.commit()
