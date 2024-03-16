import data
import conf
import requests

def post_new_order():
    return requests.post(conf.URL_SERVICE + conf.postOrder,
                        json=data.bodyOrder,
                        headers=data.headers)


response = post_new_order()
a = response.json()
print(a)
track = str(a['track'])
print(track)

