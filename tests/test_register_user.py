import pytest
import requests

from helpers import PersonData
from urls import AuthURLs


class TestRegisterUser:
    def test_create_new_user(self, create_new_user):
        response = create_new_user
        assert response[1].status_code == 200
        assert "accessToken" in response[1].json()

    def test_create_duplicate_user(self, create_new_user):
        response_new_user = create_new_user
        payload = response_new_user[0]
        response_duplicate_user = requests.post(AuthURLs.register_url, data=payload)
        assert response_duplicate_user.status_code == 403
        assert response_duplicate_user.json()["message"] == "User already exists"

    @pytest.mark.parametrize("payload", [
        PersonData.create_user_data_not_email(),
        PersonData.create_user_data_not_password(),
        PersonData.create_user_data_not_name()
    ])
    def test_create_user_not_data(self, payload):
        response = requests.post(AuthURLs.register_url, data=payload)
        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"
