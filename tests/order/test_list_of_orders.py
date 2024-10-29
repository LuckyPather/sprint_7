import allure


@allure.suite("Список заказов")
@allure.sub_suite("Список заказов")
class TestOrdersList:
    @allure.title("Вывожу список заказов")
    @allure.description("Проверяю отображение списка заказов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_list(self, order_methods):
        response = order_methods.get_orders_list()
        assert response[0] == 200 and response[1] is not None
