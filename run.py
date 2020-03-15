from iss_israel.factory import initialize_retriever
from load_config import load_config

if __name__ == '__main__':
    cfg = load_config()
    retrieve_info = initialize_retriever(cfg)
    retrieve_info.save_cities_info()
