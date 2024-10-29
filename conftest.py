import pytest

from methods.couriers_methods import Courier
from methods.order_methods import Order


@pytest.fixture()
def order_methods():
    return Order()


@pytest.fixture()
def courier_methods():
    return Courier()
