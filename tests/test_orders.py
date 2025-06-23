import allure
import pytest
import requests
import test_data


class TestOrders:
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    @allure.title("Проверяем создание нового заказа и присутствие его track в ответе")
    @allure.description("Ручка api/v1/orders")
    def test_create_order_with_various_colors(self, color, created_order):
        response = created_order(color)

        assert response.status_code == test_data.TestData.success_order_response['status_code']
        response_json = response.json()
        assert test_data.TestData.success_order_response['message'] in response_json

    @allure.title("Проверяем запрос всего списка заказов")
    @allure.description("Ручка api/v1/orders")
    def test_get_orders_list(self):

        response = requests.get(f"{test_data.TestData.ORDERS_URL}")
        assert response.status_code == test_data.TestData.success_order_list_response['status_code']
        assert isinstance(response.json().get(test_data.TestData.success_order_list_response['message']), list)
