import psycopg2
from dal import cfg
from dal.dal_interface import DalInterface


class PostgreDal(DalInterface):
    def __init__(self, database, user, password, host, port):
        self.con = psycopg2.connect(database=database,
                                    user=user,
                                    password=password,
                                    host=host,
                                    port=port,
                                    sslmode='require')

    def insert_city(self, city_name, duration, rise_time, table_name):
        cur = self.con.cursor()
        cur.execute(
            "INSERT INTO {table} (city_name,duration,rise_time) VALUES ('{city_name}', {duration}, '{rise_time}')".format(
                table=table_name, city_name=city_name, duration=duration, rise_time=rise_time))

    def commit(self):
        self.con.commit()
