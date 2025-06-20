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