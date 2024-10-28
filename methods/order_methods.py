import requests
import allure

from data import BaseUrl, OrdersData


class Order:
    def create_order(self, firstname, lastname, address, metro_station, phone, rent_time, delivery_date, comment,
                     color: list):
        data = {
            "firstName": firstname,
            "lastName": lastname,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": color
        }
        with allure.step(f"Создаю заказ с параметрами имя: {firstname}, фамилия: {lastname}, адрес: {address}, "
                         f"телефон: {phone}, кол-во дней аренды: {rent_time}, дата доставки: {delivery_date}, "
                         f"комментарий: {comment}, цвет: {color}"):
            response = requests.post(f'{BaseUrl.BASE_URL}{OrdersData.ORDERS_URL}', json=data)
        return response.status_code, response.json()

    def accept_order(self, order_id, courier_id):
        params = {
            "courierId": courier_id
        }
        with allure.step(f"Принимаю заказ с ID: {order_id} курьером: {courier_id}"):
            response = requests.put(f'{BaseUrl.BASE_URL}{OrdersData.ORDER_ACCEPT}{order_id}', params=params)
        return response.status_code, response.json()

    def get_order(self, track_number):
        params = {'t': track_number}
        with allure.step(f"Получаю информацию о заказе по номеру{track_number}"):
            response = requests.get(f'{BaseUrl.BASE_URL}{OrdersData.ORDER_TRACK}', params=params)
        return response.status_code, response.json()

    def get_orders_list(self, courier_id, nearest_station, limit, page):
        params = {
            "courierId": courier_id,
            "nearestStation": nearest_station,
            "limit": limit,
            "page": page
        }
        with allure.step(f"Получаю список заказов по переданным параметрам {courier_id}, "
                         f"{nearest_station}, {limit}, {page}"):
            response = requests.get(f"{BaseUrl.BASE_URL}{OrdersData.ORDERS_URL}", params=params)
        return response

    def cancel_order(self, track: int):
        data = {"track": track}
        with allure.step(f"Отменяю заказ под номером: {track}"):
            response = requests.put(f"{BaseUrl.BASE_URL}{OrdersData.ORDERS_URL}{OrdersData.ORDER_CANCEL}", data=data)
        return response.status_code, response.json()

    def complete_order(self, order_id):
        with allure.step(f"Завершаю заказ под номером: {order_id}"):
            response = requests.put(f"{BaseUrl.BASE_URL}{OrdersData.ORDERS_URL}{OrdersData.ORDER_FINISH}/{order_id}")
        return response.status_code, response.json()
