from dal.postgre_dal import PostgreDal
from iss_israel.iss_handler import ISSHandler
from iss_israel.retrieve_iss_info import RetrieveISSInfo


def initialize_retriever(config):
    dal = initialize_dal(config)
    api_handler = ISSHandler(config['iss']['url'])
    return RetrieveISSInfo(api_handler, dal, **config["retrieve"])


def initialize_dal(config):
    database_type = config["database_type"]
    database_config = config["databases"][database_type]
    if database_type == "postgre":
        return initialize_postgre(database_config)


def initialize_postgre(postgre_config):
    return PostgreDal(**postgre_config['connection'])
