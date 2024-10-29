import unittest
import os
import logging
# -----------------------------INFRA CLASSES---------------------------
from web_testing_projects.demoblaze.infra.config_provider import ConfigProvider
from web_testing_projects.demoblaze.infra.utilities import Utilities
from web_testing_projects.demoblaze.infra.ui.browser_wrapper import BrowserWrapper
# -----------------------------LOGIC CLASSES---------------------------
from web_testing_projects.demoblaze.logic.ui.log_in_page import LogInPage


class TestValidLogin(unittest.TestCase):
    """
    This class tests the valid login flow
    """

    def tearDown(self):
        """
        This method runs after each test
        """
        self._driver.quit()
    def test_valid_login(self):
        """
        This method tests the valid login flow
        Test_Case: TC-01
        """
        logging.info("----------------Testing Valid Login Started----------------")
        # ARRANGE
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../demoblaze.json')
        self._config = ConfigProvider().load_from_file(self._config_file_path)
        self._driver = BrowserWrapper().get_driver()
        # ACT
        login_page = LogInPage(self._driver)
        login_page.valid_login_flow()
        # ASSERT
        self.assertIn(self._config["username"], login_page.get_welcoming_message(), "Welcome message is not valid.")


if __name__ == '__main__':
    unittest.main()
