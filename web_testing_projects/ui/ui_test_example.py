import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TestGoogleWebsite(unittest.TestCase):
    """
    This class tests the search functionality of Google.
    """

    def setUp(self):
        # ARRANGE
        # Initialize the WebDriver as a Firefox instance.
        self.driver = webdriver.Chrome()
        url = "https://google.com"
        self.driver.get(url)
        self.driver.maximize_window()

    def test_demo_qa_website(self):
        """
        This method tests the search functionality of Google.
        """
        # ACT
        # Search for the assistance keyboard in Google.
        keyboard_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[2]"))
        )
        # Click on the assistance keyboard button
        keyboard_button.click()

        time.sleep(2)  # Wait for 2 seconds in order to see how it looks like

        # Search for the number 2 in Google assistance keyboard.
        number_2_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '2')]"))
        )
        # Click on the number 2 button
        number_2_button.click()
        time.sleep(2)  # Wait for 2 seconds in order to see how it looks like

        # Search for the search button
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]"))
        )
        # Click on the search button
        search_button.send_keys(Keys.ENTER)
        time.sleep(2)  # Wait for 2 seconds in order to see how it looks like

        # Search for the "לוח יד2 - דירות להשכרה, למכירה, רכב, דרושים, יד שנייה" as the
        # first result
        first_result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h3[contains(text(), 'לוח יד2 - דירות להשכרה, למכירה, רכב, דרושים, יד שנייה')]"))
        )
        time.sleep(2)
        # ASSERT
        # Verify the first result title includes the number 2
        self.assertIn("2", first_result.text, "Radio button is not selected")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()


# Run the test
if __name__ == "__main__":
    unittest.main()
