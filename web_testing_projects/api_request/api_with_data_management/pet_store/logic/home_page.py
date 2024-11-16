import json
import logging
import os
import requests
from web_testing_projects.api_request.api_with_data_management.pet_store.infra.logger_setup import LoggingSetup
from web_testing_projects.api_request.api_with_data_management.pet_store.infra.api_wrapper import ApiWrapper
from web_testing_projects.api_request.api_with_data_management.pet_store.infra.config_provider import ConfigProvider


class ApiHomePage:
    PET = "pet/"

    def __init__(self, request: ApiWrapper):
        try:
            self._request = request
            self._api = ApiWrapper()
        except Exception as e:
            logging.error(e)
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            self._config_file_path = os.path.join(base_dir, '../pet_store_data.json')
            self._config = ConfigProvider().load_from_file(self._config_file_path)
            self._url = self._config['base_url']
        except ImportError:
            logging.error("Can not open pet_store_json.json file.")

    def get_pet_by_id(self, pet_id):
        try:
            logging.info(f'Sending a get request to get a pet id: {pet_id}')
            response = self._request.get_request(
                f'{self._url}{self.PET}{pet_id}')
            if response.status_code == 200:
                return response
            else:
                logging.error(f'Get pet by id (id = 5) error: {response.status_code}')
                return None
        except requests.RequestException as e:
            logging.error(f'Get pet by id error: {e}')
            return None

    def to_dict(self, pet_id):
        return self.get_pet_by_id(pet_id).json()

    def save_pet(self, pet_id):
        try:
            with open('../pet_store_json.json', 'r') as f:
                data = json.load(f)
                if data is None:
                    data = []
                data.append(self.to_dict(pet_id))
            with open('../pet_store_json.json', 'w') as f:
                json.dump(data, f, indent=4)
                logging.info(f"Data saved successfully - pet id: {pet_id}"
                             f"\n---------------------------------------")
        except Exception as e:
            logging.error(f"Can not save config. {e}")
        except json.JSONDecodeError:
            logging.error('error in reading file')

    def get_all_pets(self):
        try:
            with open('../pet_store_json.json', 'r') as f:
                data = json.load(f)
                if data:
                    for pet in data:
                        print(f'Pet Details:\n'
                              f'pet_id = {pet['id']}\n'
                              f'pet_category = {pet['category']}\n'
                              f'pet_name = {pet['name']}\n'
                              f'pet_photoUrls = {pet['photoUrls']}\n'
                              f'pet_tags = {pet['tags']}\n'
                              f'pet_status = {pet['status']}')
                        print('---------------------------------------')
                    logging.info(f"Data loaded successfully - {len(data)} pets"
                                 f"\n---------------------------------------")
                elif data is None:
                    print("There is no data in the file")
                else:
                    logging.info("Data loaded successfully - 0 pets"
                                 f"\n---------------------------------------")
        except Exception as e:
            logging.error(f"Can not load config. {e}")
        except json.JSONDecodeError:
            logging.error('error in reading file')
