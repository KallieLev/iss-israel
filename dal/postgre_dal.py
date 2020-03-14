import psycopg2
from dal import cfg
from dal.dal_interface import DalInterface


class PostgreDal(DalInterface):
    def __init__(self):
        self.con = psycopg2.connect(database=cfg['postgre']['database'],
                                    user=cfg['postgre']['user'],
                                    password=cfg['postgre']['password'],
                                    host=cfg['postgre']['host'],
                                    port=cfg['postgre']['port'],
                                    sslmode='require')

    def insert_city(self, city_name, duration, rise_time):
        cur = self.con.cursor()
        cur.execute(
            "INSERT INTO {table} (city_name,duration,rise_time) VALUES ('{city_name}', {duration}, '{rise_time}')".format(
                table=cfg['postgre']['table_name'], city_name=city_name, duration=duration, rise_time=rise_time))

    def commit(self):
        self.con.commit()
