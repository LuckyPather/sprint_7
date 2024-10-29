import requests
import allure

from data import BaseUrl, CouriersData


class Courier:
    def create_courier(self, login, password, first_name):
        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        with allure.step(f"Создаю курьера с данными {login}, {password}, {first_name}"):
            response = requests.post(f'{BaseUrl.BASE_URL}{CouriersData.COURIERS_CREATE}', json=data)
        return response.status_code, response.json()

    def login_courier(self, login, password):
        data = {
            "login": login,
            "password": password,
        }
        with allure.step(f"Захожу в учетную запись с данными {login}, {password}"):
            response = requests.post(f'{BaseUrl.BASE_URL}{CouriersData.COURIERS_CREATE}{CouriersData.COURIERS_LOGIN}', json=data)
        return response.status_code, response.json()

    def delete_courier(self, id):
        with allure.step(f"Удаляю учетную запись c ID = {id}"):
            response = requests.delete(f'{BaseUrl.BASE_URL}{CouriersData.COURIERS_CREATE}', params=id)
        return response.status_code, response.json()
