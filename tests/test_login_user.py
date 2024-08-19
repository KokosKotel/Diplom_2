import allure
import requests

from constance import StatusMessage
from urls import AuthURLs


class TestLoginUser:
    @allure.title("Авторизация существующего пользователя")
    @allure.description("Тест проверяет успешную авторизацию существующего пользователя")
    def test_login_existing_user(self, create_new_user):
        response = create_new_user
        login_user = requests.post(AuthURLs.login_url, data=response[0])
        assert login_user.status_code == 200
        assert "accessToken" in login_user.json()

    @allure.title("Авторизация существующего пользователя с неверным email")
    @allure.description("Тест проверяет появление ошибки,"
                        "при попытке авторизоваться с неверным email")
    def test_login_user_incorrect_email(self, create_new_user):
        create_user = create_new_user
        data_user = create_user[0]
        data_user.update(
            [
                ("email", "alex@mail.ru")
            ]
        )
        response = requests.post(AuthURLs.login_url, data=data_user)
        assert response.status_code == 401
        assert response.json()["message"] == StatusMessage.incorrect_data

    @allure.title("Авторизация существующего пользователя с неверным паролем")
    @allure.description("Тест проверяет появление ошибки,"
                        "при попытке авторизоваться с неверным паролем")
    def test_login_user_incorrect_password(self, create_new_user):
        create_user = create_new_user
        data_user = create_user[0]
        data_user.update(
            [
                ("password", "password")
            ]
        )
        response = requests.post(AuthURLs.login_url, data=data_user)
        assert response.status_code == 401
        assert response.json()["message"] == StatusMessage.incorrect_data
