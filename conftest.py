import pytest
import requests
import random
import string
import test_data
import time

# генератор случайной строки
def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


# уникальные данные курьера
@pytest.fixture
def courier_data():
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()
    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }


# зарегистрированный курьер (возвращает login, password, id)
@pytest.fixture
def created_courier(courier_data):
    response = requests.post(f"{test_data.TestData.BASE_URL}/courier", data=courier_data)
    assert response.status_code == 201
    time.sleep(1)
    login_data = {
        "login": courier_data["login"],
        "password": courier_data["password"]
    }
    login_response = requests.post(f"{test_data.TestData.BASE_URL}/courier/login", data=login_data)
    assert login_response.status_code == 200
    courier_id = login_response.json().get("id")
    assert courier_id is not None

    yield {
        "login": courier_data["login"],
        "password": courier_data["password"],
        "id": courier_id
    }

    requests.delete(f"{test_data.TestData.BASE_URL}/courier/{courier_id}")


# тело заказа по умолчанию
@pytest.fixture
def base_order_payload():
    return {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "ул. Пушкина, д. 1",
        "metroStation": 4,
        "phone": "+79999999999",
        "rentTime": 5,
        "deliveryDate": "2025-06-20",
        "comment": "Тестовый заказ"
    }