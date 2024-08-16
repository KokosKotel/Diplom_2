import requests

from constance import IngredientsBurger
from urls import OrderURL


class TestCreateOrder:
    def test_create_order_auth_user(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers_user = {"Authorization": token}
        response = requests.post(OrderURL.order_url, headers=headers_user, data=IngredientsBurger.correct_burger)
        assert response.status_code == 200
        assert "order" in response.json()

    def test_create_order_not_authorized_user(self):
        response = requests.post(OrderURL.order_url, data=IngredientsBurger.correct_burger)
        assert response.status_code == 200
        assert "order" in response.json()

    def test_create_order_auth_user_incorrect_ingredients(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers_user = {"Authorization": token}
        response = requests.post(OrderURL.order_url, headers=headers_user, data=IngredientsBurger.incorrect_burger)
        assert response.status_code == 500


    def test_create_order_not_authorized_user_incorrect_ingredients(self):
        response = requests.post(OrderURL.order_url, data=IngredientsBurger.incorrect_burger)
        assert response.status_code == 500


    def test_create_order_auth_user_not_ingredients(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers_user = {"Authorization": token}
        response = requests.post(OrderURL.order_url, headers=headers_user, data=IngredientsBurger.not_ingredients_burger)
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    def test_create_order_not_authorized_user_not_ingredients(self):
        response = requests.post(OrderURL.order_url, data=IngredientsBurger.not_ingredients_burger)
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"
