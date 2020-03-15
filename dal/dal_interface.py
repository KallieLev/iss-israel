from abc import ABC, abstractmethod


class DalInterface(ABC):
    @abstractmethod
    def insert_city(self, city_name, duration, rise_time, table_name):
        pass
