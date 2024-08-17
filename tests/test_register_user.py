import allure
import pytest
import requests

from constance import StatusMessage
from helpers import PersonData
from urls import AuthURLs


class TestRegisterUser:
    @allure.title("Успешное создание пользователя")
    @allure.description("Тест проверяет успешное создание нового пользователя")
    def test_create_new_user(self, create_new_user):
        response = create_new_user
        assert response[1].status_code == 200
        assert "accessToken" in response[1].json()

    @allure.title("Создание существующего пользователя")
    @allure.description("Тест проверяет появление ошибки, при попытке создать"
                        "пользователя с данными, ранее созданного пользователя")
    def test_create_duplicate_user(self, create_new_user):
        response_new_user = create_new_user
        payload = response_new_user[0]
        response_duplicate_user = requests.post(AuthURLs.register_url, data=payload)
        assert response_duplicate_user.status_code == 403
        assert response_duplicate_user.json()["message"] == StatusMessage.duplicate_user

    @allure.title("Создание пользователя без заполнения одного из обязательных полей")
    @allure.description("Тест проверяет появление ошибки, при попытке создать"
                        "пользователя без заполнения одного из обязательных полей")
    @pytest.mark.parametrize("payload", [
        PersonData.create_user_data_not_email(),
        PersonData.create_user_data_not_password(),
        PersonData.create_user_data_not_name()
    ])
    def test_create_user_not_data(self, payload):
        response = requests.post(AuthURLs.register_url, data=payload)
        assert response.status_code == 403
        assert response.json()["message"] == StatusMessage.not_field_data
