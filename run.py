import json

from iss_israel.factory import initialize_retriever

if __name__ == '__main__':
    with open('config.json', 'r') as config_file:
        cfg = json.load(config_file)

    retrieve_info = initialize_retriever(cfg)
    retrieve_info.save_cities_info()
