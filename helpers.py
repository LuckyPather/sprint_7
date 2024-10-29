import requests
import random
import string
from faker import Faker
import re

from data import OrdersData


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def register_new_courier_and_return_login_password():

    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass, response.json()


# Вызываем из теста
class GeneratorOrder:
    def __init__(self):
        fake = Faker('ru_RU')
        self.name = fake.first_name()
        self.surname = fake.last_name()
        self.address = "Москва, тест, тест"
        self.metro_station = random.randint(1, 4)
        self.phone_number = random.choice(OrdersData.phone_numbers)
        self.data = "01.10.2024"
        self.option_term = random.randint(1, 5)
        self.colors = ["BLACK", "GREY"]
        self.comment = "тест"


class GeneratorCouriers:
    def __init__(self):
        self.login = generate_random_string(10)
        self.password = generate_random_string(10)
        self.first_name = generate_random_string(10)
