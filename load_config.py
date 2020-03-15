import json


def load_config():
    with open('config.json', 'r') as config_file:
        cfg = json.load(config_file)
    return cfg
