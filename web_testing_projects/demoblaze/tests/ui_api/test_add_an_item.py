import unittest
import os
import logging
import time
# ----------------------------- INFRA CLASSES -----------------------------
from web_testing_projects.demoblaze.infra.config_provider import ConfigProvider
from web_testing_projects.demoblaze.infra.api.api_wrapper import ApiWrapper
from web_testing_projects.demoblaze.infra.ui.browser_wrapper import BrowserWrapper
# ----------------------------- LOGIC CLASSES -----------------------------
from web_testing_projects.demoblaze.logic.api.home_page import HomePage
from web_testing_projects.demoblaze.logic.ui.log_in_page import LogInPage


class TestAddAnItem(unittest.TestCase):

    def tearDown(self):
        """
        This method runs after every test
        """
        self._driver.quit()

    def test_add_an_item(self):
        """
        This method tests the add an item
        Test_Case: TC-02
        """
        logging.info("----------------Testing Add an Item Started----------------")
        # ARRANGE
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../demoblaze.json')
        self._config = ConfigProvider().load_from_file(self._config_file_path)
        self._driver = BrowserWrapper().get_driver()
        self._api = ApiWrapper()
        # ACT
        login_page = LogInPage(self._driver)
        login_page.valid_login_flow()
        time.sleep(5)
        # cookie = login_page.valid_login_flow()
        api_home_page = HomePage(self._api)
        post_request = api_home_page.add_an_item()
        self.assertTrue(post_request.ok, "Post request has not been sent.")
        self.assertEqual(post_request.status_code, 200, "Status code is not 200.")


if __name__ == '__main__':
    unittest.main()
