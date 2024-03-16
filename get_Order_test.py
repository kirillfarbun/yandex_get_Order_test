import conf
import requests
import post_Order
# Кирилл Фарбун, 14-я когорта — Финальный проект. Инженер по тестированию плюс
def get_Order():
    return requests.get(conf.URL_SERVICE + conf.getOrder + post_Order.track)


def positive_assert(code):
    response = get_Order()
    assert response.status_code == code


def test_status_code():
    positive_assert(200)