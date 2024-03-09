import pytest
from last_five_operations import get_last_five_operations


def test_get_last_five_operations():
    # В тесте сравниваем фактический вывод функции с ожидаемым результатом
    expected_output = [
        "16.03.2022 Пополнение счета", "Счет **6299 -> PayPal", "45983.74 руб.",
        "13.03.2022 Перевод другу", "Visa **8542 -> **6683", "1200.0 руб.",
        "26.02.2022 Оплата услуг", "Сбербанк Страхование -> Счет **5166", "2567.99 руб.",
        "21.02.2022 Покупка в интернет-магазине", "ottostore.ru -> Visa **6381", "14900.0 руб.",
        "17.02.2022 Перевод маме", "Visa **6381 -> **9134", "2000.0 руб."
    ]

    actual_output = get_last_five_operations('operations.zip')

    assert actual_output == expected_output