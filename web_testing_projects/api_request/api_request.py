import requests

url = "https://www.selenium.dev/about/"

response = requests.get(url)
print(response.status_code)
print(response.ok)

# Another example
url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

response = requests.get(url)
response_data = response.json()
print(response_data)


