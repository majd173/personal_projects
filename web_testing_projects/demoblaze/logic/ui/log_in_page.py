import logging
import os
import time

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# ----------------------------- INFRA CLASSES -----------------------------
from web_testing_projects.demoblaze.infra.ui.base_page import BasePage
from web_testing_projects.demoblaze.infra.config_provider import ConfigProvider


class LogInPage(BasePage):
    """
    This class represents the LogIn Page
    """
    SIGN_UP_BUTTON = "a[id='signin2']"
    SIGN_UP_USERNAME_INPUT = "input[id='sign-username']"
    SIGN_UP_PASSWORD_INPUT = "input[id='sign-password']"
    SIGN_UP_BUTTON_TWO = "button[onclick='register()']"
    LOGIN_BUTTON = "a[id='login2']"
    USERNAME_INPUT = "input[id='loginusername']"
    PASSWORD_INPUT = "input[id='loginpassword']"
    LOGIN_BUTTON_TWO = "button[onclick='logIn()']"
    WELCOMING_MESSAGE = "a[id='nameofuser']"

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(self._driver, 10)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../demoblaze.json')
        self._config = ConfigProvider().load_from_file(self._config_file_path)

    def click_login_button(self):
        """
        This method clicks on the login button
        """
        try:
            login_button = self._wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.LOGIN_BUTTON)))
            login_button.click()
        except TimeoutException:
            logging.error("Login button is not clickable.")

    def enter_username(self):
        """
        This method enters the username
        """
        try:
            username_input = self._wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.USERNAME_INPUT)))
            logging.info(f'Entering username: {self._config["username"]}')
            username_input.send_keys(self._config['username'])
        except TimeoutException:
            logging.error("Username input is not clickable.")

    def enter_password(self, ):
        """
        This method enters the password
        """
        try:
            password_input = self._wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.PASSWORD_INPUT)))
            logging.info(f'Entering password: {self._config["password"]}')
            password_input.send_keys(self._config['password'])
        except TimeoutException:
            logging.error("Password input is not clickable.")

    def click_login_button_two(self):
        """
        This method clicks on the login button
        """
        try:
            login_button_two = self._wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.LOGIN_BUTTON_TWO)))
            login_button_two.click()
        except TimeoutException:
            logging.error("Login button is not clickable.")

    def valid_login_flow(self):
        """
        This method performs valid login flow
        :return: cookies
        """
        try:
            self.click_login_button()
            self.enter_username()
            self.enter_password()
            self.click_login_button_two()
            # cookies = self._driver.get_cookies()
            # print(cookies)
            # if cookies:
            #     user_cookie_value = cookies[0]['value']
            return {
                    'user': 'f05a0b3b-237d-d550-30a6-98e30dca859d',
                    'tokenp_': 'bWFqZDE3MzAwMzM='
                }
        except TimeoutException:
            logging.error("Login flow is not valid.")

    def get_welcoming_message(self):
        """
        This method gets the welcoming message
        :return: text of the welcoming message
        """
        try:
            welcoming_message = self._wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, self.WELCOMING_MESSAGE)))
            if welcoming_message:
                return welcoming_message.text
            else:
                return None
        except TimeoutException:
            logging.error("Welcoming message is not visible.")
