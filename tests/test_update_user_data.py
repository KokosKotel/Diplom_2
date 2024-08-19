import allure
import pytest
import requests

from helpers import PersonData
from urls import AuthURLs


class TestUpdateUserData:
    @allure.title("Изменение данных авторизованным пользователем")
    @allure.description("Тест проверяет успешное изменение данных пользователя")
    @pytest.mark.parametrize("data_user", [
        PersonData.create_user_data()["email"],
        PersonData.create_user_data()["password"],
        PersonData.create_user_data()["name"]
    ])
    def test_update_user_data(self, create_new_user, data_user):
        token = create_new_user[1].json()["accessToken"]
        headers_user = {"Authorization": token}
        response = requests.patch(AuthURLs.user_url, headers=headers_user, data=data_user)
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title("Изменение данных неавторизованным пользователем")
    @allure.description("Тест проверяет появление ошибки, при попытки"
                        "изменить данные неавторизованным пользователем")
    @pytest.mark.parametrize("data_user", [
        PersonData.create_user_data()["email"],
        PersonData.create_user_data()["password"],
        PersonData.create_user_data()["name"]
    ])
    def test_update_user_data_not_authorized(self, data_user):
        response = requests.patch(AuthURLs.user_url, data=data_user)
        assert response.status_code == 401
        assert response.json()["success"] == False
