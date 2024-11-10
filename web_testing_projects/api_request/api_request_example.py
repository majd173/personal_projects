import requests


#
# url = "https://www.ynet.co.il/iphone/json/api/talkbacks/add"
#
# data = {
#     "talkback_title": "ישמור",
#     "talkback_content": "111",
#     "author_name": "ישראלי",
#     "author_email": "",
#     "author_location": "",
#     "article_id": "sy1ufcszyg",
#     "talkbackParentData": "",
#     "talkback_source": None
# }
#
# response = requests.post(url, data=data)
# print(response.status_code)


# ----------------------------------------------------------------------

# Example 2:

def response_2():
    url_2 = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/buzz/posts"
    data_2 = {
        "type": "text",
        "text": "e"
    }
    cookies = {
        'orangehrm': 'emd5197n1nd1ia1g33k90u6lhp'
    }
    response = requests.post(url_2, data=data_2, cookies=cookies)
    return response


def performance_test():
    count = 0
    while count < 10:
        response_2()
        count += 1


performance_test()
