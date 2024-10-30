import requests
url = "https://www.selenium.dev/about/"

response = requests.get(url)
print(response.status_code)
print(response.ok)
