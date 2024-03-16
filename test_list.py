import sender_stand_request

# Кирилл Фарбун, 14-я когорта — Финальный проект. Инженер по тестированию плюс

# Тест создает заказ вызывая функцию "sender_stand_request.post_new_order()" и записывает результат выполнения функции
# в переменную "post_response"
# в переменную "а" записывается json ответ и номер заказа присваивается переменной "track"
# вызвается функция получания заказа по номеру "sender_stand_request.get_order(track)" и записывает результат выполнения функци
# в переменную get_response


def positive_assert(code):
    post_response = sender_stand_request.post_new_order()
    a = post_response.json()
    track = str(a['track'])
    get_response = sender_stand_request.get_order(track)
    assert get_response.status_code == code


def test_get_order_by_track_success():
    positive_assert(200)

# изменено названий переменных и функций