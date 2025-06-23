class TestData:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

    COURIER_URL = f"{BASE_URL}/courier"
    LOGIN_URL = f"{BASE_URL}/courier/login"
    ORDERS_URL = f"{BASE_URL}/orders"
    CANCEL_URL = f"{BASE_URL}/orders/cancel"

    base_order_payload= {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "ул. Пушкина, д. 1",
            "metroStation": 4,
            "phone": "+79999999999",
            "rentTime": 5,
            "deliveryDate": "2025-06-20",
            "comment": "Тестовый заказ"
        }

    success_login_response = {'status_code' : 200, 'message' : "id"}
    wrong_password_login_response = {'status_code': 404, 'message' : "Учетная запись не найдена"}
    missing_data_login_response = {'status_code': 400, 'message': "Недостаточно данных"}

    success_order_response = {'status_code': 201, 'message' : "track"}
    success_order_list_response = {'status_code': 200, 'message': "orders"}

    success_create_courier_response = {'status_code': 201, 'message': "ok"}
    double_data_create_courier_response = {'status_code': 409, 'message': "Этот логин уже используется"}
    missing_data_create_courier_response = {'status_code': 400, 'message': "Недостаточно данных"}