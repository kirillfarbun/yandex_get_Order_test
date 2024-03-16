import data
import conf
import requests


def post_new_order():
    return requests.post(conf.URL_SERVICE + conf.POST_ORDER,
                        json=data.body_order,
                        headers=data.headers)


def get_order(track):
    return requests.get(conf.URL_SERVICE + conf.GET_ORDER + track)

# изменено названий переменных и функций