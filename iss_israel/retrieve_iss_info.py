from utils.timestamp_helper import convert_timezone


class RetrieveISSInfo:
    def __init__(self, api_handler, dal, **kwargs):
        self.api_handler = api_handler
        self.dal = dal
        self.cities = kwargs['cities']
        self.number_of_events = kwargs['number_of_events']
        self.from_timezone = kwargs['from_timezone']
        self.to_timezone = kwargs['to_timezone']
        self.table_name = kwargs['table_name']

    def get_cities_info(self):
        cities_info = {}
        cities = self.cities
        for city in cities.keys():
            info = self.api_handler.get_timestamps(cities[city]['latitude'], cities[city]['longitude'],
                                                   self.number_of_events)
            cities_info[city] = info
        return cities_info

    def save_cities_info(self):
        cities_info = self.get_cities_info()
        for city, info in cities_info.items():
            for event in info:
                rise_time = convert_timezone(event['risetime'], self.from_timezone,
                                             self.to_timezone)
                self.dal.insert_city(city, event['duration'], rise_time, self.table_name)

        self.dal.commit()
