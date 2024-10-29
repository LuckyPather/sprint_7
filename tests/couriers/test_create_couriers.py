import pytest
import allure

from helpers import register_new_courier_and_return_login_password, GeneratorCouriers


@allure.suite("Курьер")
@allure.sub_suite("Регистрация курьера")
class TestCourierRegister:
    @allure.title("Создаю Курьера")
    @allure.description("Проверяю создание курьера")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_courier(self):
        data = register_new_courier_and_return_login_password()
        assert len(data[0]) == 3 and data[1] == {"ok": True}

    @allure.title("Создаю 2 одинаковых Курьеров")
    @allure.description("Проверяю возникновение ошибки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_two_identical_courier(self, courier_methods):
        data = register_new_courier_and_return_login_password()
        response = courier_methods.create_courier(data[0][0], data[0][1], data[0][2])
        assert (response[1]["code"] == 409 and
                response[1]["message"] == "Этот логин уже используется. Попробуйте другой.")

    @allure.title("Создаю Курьеров без указания обязательных полей")
    @allure.description("Проверяю возникновение ошибки")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("login, password, first_name",
                             [
                                 (GeneratorCouriers().login, '', GeneratorCouriers().first_name),
                                 ('', GeneratorCouriers().password, GeneratorCouriers().first_name),
                             ])
    def test_create_courier_without_required_field(self, courier_methods, login, password, first_name):
        response = courier_methods.create_courier(login, password, first_name)
        assert (response[1]['code'] == 400 and
                response[1]['message'] == 'Недостаточно данных для создания учетной записи')
