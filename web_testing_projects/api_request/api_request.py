import requests
import unittest


# An example of an api get request test.
class TestFlukeApi(unittest.TestCase):
    def test_get_request(self):
        url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, "Status code is not 200")
        self.assertTrue(response.ok, "Response is not ok")
