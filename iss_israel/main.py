from iss_israel.retrieve_iss_info import RetrieveISSInfo

if __name__ == '__main__':
    retrieve_info = RetrieveISSInfo()
    retrieve_info.insert_cities_info_postgre()