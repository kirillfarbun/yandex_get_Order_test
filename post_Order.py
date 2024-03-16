import data
import conf
import requests

def post_new_order():
    return requests.post(conf.URL_SERVICE + conf.postOrder,
                        json=data.bodyOrder,
                        headers=data.headers)


response = post_new_order()

track = str(response.json()["track"])

