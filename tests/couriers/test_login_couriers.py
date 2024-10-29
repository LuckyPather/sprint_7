import pytest
import allure

from helpers import register_new_courier_and_return_login_password, GeneratorCouriers


@allure.suite("Курьер")
@allure.sub_suite("Логин курьера")
class TestCouriersLogin:
    @allure.title("Успешный вход в аккаунт")
    @allure.description("Проверяю вход с валидными данными")
    @allure.severity(allure.severity_level.NORMAL)
    def test_success_login(self, courier_methods):
        data = register_new_courier_and_return_login_password()
        response = courier_methods.login_courier(data[0][0], data[0][1])
        assert response[0] == 200 and response[1] is not None

    @pytest.mark.parametrize("login, password",
                             [
                                 (GeneratorCouriers().login, ''),
                                 ('', GeneratorCouriers().password),
                             ])
    @allure.title("Вход без обязательных полей")
    @allure.description("Проверяю возникновение ошибки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_without_required_fields(self, courier_methods, login, password):
        response = courier_methods.login_courier(login, password)
        assert response[0] == 400 and response[1]["message"] == "Недостаточно данных для входа"

    @allure.title("Вход с невалидными данными")
    @allure.description("Проверяю возникновение ошибки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_wrong_login(self, courier_methods):
        response = courier_methods.login_courier(GeneratorCouriers().login, GeneratorCouriers().password)
        assert response[0] == 404 and response[1]["message"] == "Учетная запись не найдена"
