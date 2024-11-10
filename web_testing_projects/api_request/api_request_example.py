import requests

url = "https://www.ynet.co.il/iphone/json/api/talkbacks/add"

data = {
  "talkback_title": "ישמור",
  "talkback_content": "111",
  "author_name": "ישראלי",
  "author_email": "",
  "author_location": "",
  "article_id": "sy1ufcszyg",
  "talkbackParentData": "",
  "talkback_source": None
}

response = requests.post(url, data=data)
print(response.status_code)