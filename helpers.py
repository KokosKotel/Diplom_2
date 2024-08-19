import allure
from faker import Faker


class PersonData:
    @staticmethod
    @allure.title("Создает фейк данные пользователя")
    def create_user_data(email=True, password=True, name=True):
        faker = Faker()
        data = {}
        if email:
            data["email"] = faker.email()
        if password:
            data["password"] = faker.password()
        if name:
            data["name"] = faker.name()
        return data
