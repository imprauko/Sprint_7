import allure
import requests
import pytest
import test_data

class TestCourierCreation:
    @allure.title("Проверяем создание нового курьера")
    @allure.description("Ручка api/v1/courier")
    def test_create_courier_success(self, courier_data):
        response = requests.post(f"{test_data.TestData.COURIER_URL}", data=courier_data)
        assert response.status_code == test_data.TestData.success_create_courier_response['status_code']
        assert response.json().get(test_data.TestData.success_create_courier_response['message']) is True


    @allure.title("Проверяем невозможность создания дубля курьера")
    @allure.description("Ручка api/v1/courier")
    def test_create_duplicate_courier(self, created_courier):
        duplicate_data = {
            "login": created_courier[0]["login"],
            "password": created_courier[0]["password"],
            "firstName": "Любой"
        }
        response = requests.post(f"{test_data.TestData.COURIER_URL}", data=duplicate_data)
        assert response.status_code == test_data.TestData.double_data_create_courier_response['status_code']
        assert test_data.TestData.double_data_create_courier_response['message'] in response.text

    #поле Name - не обязательно
    @allure.title("Проверка обязательности поля Login и Password при создании нового курьера")
    @allure.description("Ручка api/v1/courier")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_fields(self, missing_field, courier_data):

        courier_data.pop(missing_field)
        response = requests.post(f"{test_data.TestData.COURIER_URL}", data=courier_data)
        assert response.status_code == test_data.TestData.missing_data_create_courier_response['status_code']
        assert test_data.TestData.missing_data_create_courier_response['message'] in response.text
