import allure
from faker import Faker


class PersonData:
    @staticmethod
    @allure.title("Создает фейк данные пользователя")
    def create_user_data():
        faker = Faker()
        data = {
            'email': faker.email(),
            'password': faker.password(),
            'name': faker.first_name()
        }
        return data

    @staticmethod
    @allure.title("Создает фейк данные пользователя без email")
    def create_user_data_not_email():
        faker = Faker()
        data = {
            "password": faker.password(),
            "name": faker.name()
        }
        return data

    @staticmethod
    @allure.title("Создает фейк данные пользователя без пароля")
    def create_user_data_not_password():
        faker = Faker()
        data = {
            "email": faker.email(),
            "name": faker.name()
        }
        return data

    @staticmethod
    @allure.title("Создает фейк данные пользователя без имени")
    def create_user_data_not_name():
        faker = Faker()
        data = {
            "email": faker.email(),
            "password": faker.password()
        }
        return data
