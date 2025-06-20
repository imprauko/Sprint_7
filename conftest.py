import copy

import pytest
import requests
import random
import string
import test_data


# уникальные данные курьера
@pytest.fixture
def courier_data():
    def generate_random_string(length=10):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()
    login_data = {
        "login": login,
        "password": password
    }

    yield {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    login_response = requests.post(f"{test_data.TestData.LOGIN_URL}", data=login_data)
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        requests.delete(f"{test_data.TestData.COURIER_URL}/{courier_id}")


# зарегистрированный курьер (возвращает login, password, id)
@pytest.fixture
def created_courier(courier_data):
    response = requests.post(f"{test_data.TestData.COURIER_URL}", data=courier_data)
    assert response.status_code == 201

    login_data = {
        "login": courier_data["login"],
        "password": courier_data["password"]
    }
    login_response = requests.post(f"{test_data.TestData.LOGIN_URL}", data=login_data)

    courier_id = login_response.json().get("id")

    yield {
        "login": courier_data["login"],
        "password": courier_data["password"],
        "id": courier_id
    }

    requests.delete(f"{test_data.TestData.COURIER_URL}/{courier_id}")

@pytest.fixture
def created_order():
    created_tracks = []

    def wrapper(color_list):
        payload = copy.deepcopy(test_data.TestData.base_order_payload)
        payload["color"] = color_list
        response = requests.post(f"{test_data.TestData.ORDERS_URL}", json=payload)
        created_tracks.append(response)
        return response

    yield wrapper

    for response in created_tracks:
        track = response.json().get("track")
        if track:
            requests.put(f"{test_data.TestData.CANCEL_URL}", params={"track": track})