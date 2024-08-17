import allure
import pytest
import requests

from helpers import PersonData
from urls import AuthURLs


@pytest.fixture
@allure.title("Создает пользователя и удаляет его после теста")
def create_new_user():
    payload = PersonData.create_user_data()
    response = requests.post(AuthURLs.register_url, data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(AuthURLs.user_url, headers={"Authorization": token})
