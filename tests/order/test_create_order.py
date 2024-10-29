import pytest
import allure

from helpers import GeneratorOrder


@allure.suite("Заказ")
@allure.sub_suite("Создание заказа")
class TestCreateOrder:

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('color', (
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            []))
    def test_create_order(self, order_methods, color):
        allure.dynamic.title(f"Создаю заказ с цветом {color}")
        allure.dynamic.description(f"Проверяю создание заказа с цветом {color}")
        order = GeneratorOrder()
        response = order_methods.create_order(firstname=order.name, lastname=order.surname, address=order.address,
                                              metro_station=order.metro_station, phone=order.phone_number,
                                              rent_time=order.option_term, delivery_date=order.data,
                                              comment=order.comment, color=color)

        assert response[0] == 201 and response[1]['track'] is not None
