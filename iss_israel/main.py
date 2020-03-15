from iss_israel.retrieve_iss_info import RetrieveISSInfo
from dal.postgre_dal import PostgreDal
from iss_israel.iss_handler import ISSHandler

if __name__ == '__main__':
    api_handler = ISSHandler(cfg['iss']['url'])
    dal = PostgreDal(database=cfg['postgre']['database'],
                     user=cfg['postgre']['user'],
                     password=cfg['postgre']['password'],
                     host=cfg['postgre']['host'],
                     port=cfg['postgre']['port'])
    retrieve_info = RetrieveISSInfo(api_handler, dal)
    retrieve_info.save_cities_info()
