import allure
import pytest
import requests
import test_data

@pytest.mark.parametrize("color", [
    ["BLACK"],
    ["GREY"],
    ["BLACK", "GREY"],
    []
])
@allure.title("Проверяем создание нового заказа и присутствие его track в ответе")
@allure.description("Ручка api/v1/orders")
def test_create_order_with_various_colors(color, base_order_payload):
    base_order_payload["color"] = color
    response = requests.post(f"{test_data.TestData.ORDERS_URL}", json=base_order_payload)
    assert response.status_code == 201
    assert "track" in response.json()
    check_track = response.json()
    track = check_track['track']
    cancel_response = requests.put(f"{test_data.TestData.CANCEL_URL}", params={"track": track})
    assert cancel_response.status_code == 200

@allure.title("Проверяем запрос всего списка заказов")
@allure.description("Ручка api/v1/orders")
def test_get_orders_list(base_order_payload):

    response = requests.get(f"{test_data.TestData.ORDERS_URL}")
    assert response.status_code == 200
    assert isinstance(response.json().get("orders"), list)
