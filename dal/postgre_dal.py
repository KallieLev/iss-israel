import psycopg2

from dal.dal_interface import DalInterface


class PostgreDal(DalInterface):
    def __init__(self, **kwargs):
        self.con = psycopg2.connect(**kwargs)

    def insert_city(self, city_name, duration, rise_time, table_name):
        cur = self.con.cursor()
        cur.execute(
            "INSERT INTO {table} (city_name,duration,rise_time) VALUES ('{city_name}', {duration}, '{rise_time}')".format(
                table=table_name, city_name=city_name, duration=duration, rise_time=rise_time))

    def commit(self):
        self.con.commit()
