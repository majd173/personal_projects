import logging
import requests
import os
# ----------------------------- INFRA CLASSES -----------------------------
from web_testing_projects.demoblaze.infra.config_provider import ConfigProvider
from web_testing_projects.demoblaze.infra.api.api_wrapper import ApiWrapper


class HomePage:
    """
    This class represents the API requests
    """
    ADD_ITEM = "addtocart"
    MONITORS = "bycat"

    def __init__(self, request: ApiWrapper):
        try:
            self._request = request
            self._api = ApiWrapper()
            base_dir = os.path.dirname(os.path.abspath(__file__))
            self._config_file_path = os.path.join(base_dir, '../../demoblaze.json')
            self._config = ConfigProvider().load_from_file(self._config_file_path)
            self._url = self._config['base_url']
        except ImportError:
            logging.error("Can not open demoblaze.json file.")

    def add_an_item(self):
        """
        This method adds an item to cart
        :return: response
        """
        try:
            logging.info("Sending a post request to add an item to cart.")
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Referer': 'https://www.demoblaze.com',
            }

            cookies = {
                'tokenp_': 'bWFqZDE3MzAyNzE=',
                'user': 'd59a5c5f-0f2a-83f9-e47c-4a87eb0f4aea'
            }
            body = {
                "id": "ad73c683-5152-627d-50e3-33f16ecb5580",
                "cookie": "bWFqZDE3MzAwMzM=",
                "prod_id": "9",
                "flag": "true"
            }
            response = self._request.post_request(
                f'{self._url}{self.ADD_ITEM}',
                headers,
                cookies,
                body)
            return response
        except requests.exceptions.RequestException as e:
            logging.error(f'post request has not been sent.: {e}')

    def receive_monitors(self, cookie):
        """
        This method receives monitors
        :param cookie:
        :return: response
        """
        try:
            logging.info("Sending a get request to receive monitors.")
            body = {
                "cat": "Monitor"
            }
            response = self._request.get_request(
                f'{self._url}{self.MONITORS}',
                cookie,
                body)
            return response
        except requests.exceptions.RequestException as e:
            logging.error(f'get request has not been sent.: {e}')
