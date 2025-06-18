import allure
import requests
import pytest
import test_data

@allure.title("Проверяем успешность логина курьера и присутствие его id в ответе")
@allure.description("Ручка api/v1/courier/login")
def test_login_courier_success(created_courier):
    login_data = {
        "login": created_courier["login"],
        "password": created_courier["password"]
    }
    response = requests.post(f"{test_data.TestData.LOGIN_URL}", data=login_data)
    assert response.status_code == 200
    assert "id" in response.json()

@allure.title("Проверяем невозможность логина с неправильным паролем и ответ - Учетная запись не найдена")
@allure.description("Ручка api/v1/courier/login")
def test_login_with_wrong_password(created_courier):
    response = requests.post(f"{test_data.TestData.LOGIN_URL}", data={
        "login": created_courier["login"],
        "password": "wrongpassword"
    })
    assert response.status_code == 404
    assert "Учетная запись не найдена" in response.text

@allure.title("Проверяем невозможность логина курьера при отсутствии логина или пароля")
@allure.description("Ручка api/v1/courier/login")
@pytest.mark.parametrize("missing_field", ["login", "password"])
def test_login_missing_field(missing_field, created_courier):
    data = {}
    if missing_field != "login":
        data["login"] = created_courier["login"]
    if missing_field != "password":
        data["password"] = created_courier["password"]

    response = requests.post(f"{test_data.TestData.LOGIN_URL}", json=data)
    assert response.status_code == 400
    assert "Недостаточно данных" in response.text
