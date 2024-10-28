import requests
import random
import string
from faker import Faker
import re

from data import OrdersData


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
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
    return login_pass


# Вызываем из теста
class GeneratorOrder:
    def __init__(self):
        fake = Faker('ru_RU')
        self.name = fake.first_name()
        self.surname = fake.last_name()
        self.address = re.sub(r'[^a-яА-Я0-9\s,]', '', fake.address())
        self.metro_station = random.randint(1, 5)
        self.phone_number = random.choice(OrdersData.phone_numbers)
        self.data = fake.date_this_month().strftime('%d.%m.%Y')
        self.option_term = random.randint(1, 5)
        self.colors = random.choice(["BLACK", "GREY"])
        self.comment = fake.sentence()
