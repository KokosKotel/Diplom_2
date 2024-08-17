import allure
import requests

from constance import IngredientsBurger, StatusMessage
from urls import OrderURL


class TestCreateOrder:
    @allure.title("Авторизованный пользователь создает заказ")
    @allure.description("Тест проверяет, что заказ был успешно создан")
    def test_create_order_auth_user(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers_user = {"Authorization": token}
        response = requests.post(OrderURL.order_url, headers=headers_user, data=IngredientsBurger.correct_burger)
        assert response.status_code == 200
        assert "order" in response.json()

    @allure.title("Неавторизованный пользователь создает заказ")
    @allure.description("Тест проверяет, что заказ был успешно создан")
    def test_create_order_not_authorized_user(self):
        response = requests.post(OrderURL.order_url, data=IngredientsBurger.correct_burger)
        assert response.status_code == 200
        assert "order" in response.json()

    @allure.title("Ошибка при попытке создать заказ авторизованным пользователем с неверным хешем ингредиентов")
    @allure.description("Тест проверяет, что при заказе с неверным хешом"
                        "ингредиентов, появляется ошибка")
    def test_create_order_auth_user_incorrect_ingredients(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers_user = {"Authorization": token}
        response = requests.post(OrderURL.order_url, headers=headers_user, data=IngredientsBurger.incorrect_burger)
        assert response.status_code == 500

    @allure.title("Ошибка при попытке создать заказ неавторизованным пользователем с неверным хешем ингредиентов")
    @allure.description("Тест проверяет, что при заказе с неверным хешом"
                        "ингредиентов, появляется ошибка")
    def test_create_order_not_authorized_user_incorrect_ingredients(self):
        response = requests.post(OrderURL.order_url, data=IngredientsBurger.incorrect_burger)
        assert response.status_code == 500

    @allure.title("Ошибка при попытке создать заказ авторизованным пользователем без ингредиентов")
    @allure.description("Тест проверяет, что при заказе без ингредиентов,"
                        "появляется ошибка")
    def test_create_order_auth_user_not_ingredients(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers_user = {"Authorization": token}
        response = requests.post(OrderURL.order_url, headers=headers_user, data=IngredientsBurger.not_ingredients_burger)
        assert response.status_code == 400
        assert response.json()["message"] == StatusMessage.not_id_ingredients

    @allure.title("Ошибка при попытке создать заказ неавторизованным пользователем без ингредиентов")
    @allure.description("Тест проверяет, что при заказе без ингредиентов,"
                        "появляется ошибка")
    def test_create_order_not_authorized_user_not_ingredients(self):
        response = requests.post(OrderURL.order_url, data=IngredientsBurger.not_ingredients_burger)
        assert response.status_code == 400
        assert response.json()["message"] == StatusMessage.not_id_ingredients
