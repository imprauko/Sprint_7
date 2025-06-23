import allure
import requests
import pytest
import test_data

class TestLoginCourier:
    @allure.title("Проверяем успешность логина курьера и присутствие его id в ответе")
    @allure.description("Ручка api/v1/courier/login")
    def test_login_courier_success(self, created_courier):
        login_data = {
            "login": created_courier[0]["login"],
            "password": created_courier[0]["password"]
        }
        response = requests.post(f"{test_data.TestData.LOGIN_URL}", data=login_data)
        assert response.status_code == test_data.TestData.success_login_response['status_code']
        assert test_data.TestData.success_login_response['message'] in response.json()

    @allure.title("Проверяем невозможность логина с неправильным паролем и ответ - Учетная запись не найдена")
    @allure.description("Ручка api/v1/courier/login")
    def test_login_with_wrong_password(self, created_courier):
        response = requests.post(f"{test_data.TestData.LOGIN_URL}", data={
            "login": created_courier[0]["login"],
            "password": "wrongpassword"
        })
        assert response.status_code == test_data.TestData.wrong_password_login_response['status_code']
        assert test_data.TestData.wrong_password_login_response['message'] in response.text

    @allure.title("Проверяем невозможность логина курьера при отсутствии логина или пароля")
    @allure.description("Ручка api/v1/courier/login")
    @pytest.mark.parametrize('data_number', [1, 2])
    def test_login_missing_field(self, data_number, created_courier):

        response = requests.post(f"{test_data.TestData.LOGIN_URL}", json=created_courier[data_number])
        assert response.status_code == test_data.TestData.missing_data_login_response['status_code']
        assert test_data.TestData.missing_data_login_response['message'] in response.text
