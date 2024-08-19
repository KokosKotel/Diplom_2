import allure
import requests

from constance import IngredientsBurger, StatusMessage
from urls import OrderURL


class TestGetOrder:
    @allure.title("Авторизованный пользователь получает список заказов")
    @allure.description("Тест проверяет, что авторизованный пользователь"
                        "получает список заказов")
    def test_get_order_authorized(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers_user = {"Authorization": token}
        create_order = requests.post(OrderURL.order_url, headers=headers_user, data=IngredientsBurger.correct_burger)
        number_order = create_order.json()["order"].get("number")
        response_get_order = requests.get(OrderURL.order_url, headers=headers_user)
        assert response_get_order.status_code == 200
        assert number_order == response_get_order.json()["orders"][0]["number"]

    @allure.title("Ошибка при попытке получить список заказов неавторизованным пользователем")
    @allure.description("Тест проверяет появление ошибки, при попытке"
                        "получить список заказов неавторизованным пользователем")
    def test_get_order_not_authorized(self):
        response = requests.get(OrderURL.order_url)
        assert response.status_code == 401
        assert response.json()["message"] == StatusMessage.not_authorised
