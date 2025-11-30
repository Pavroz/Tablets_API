from data import test_data
import pytest
import allure

@allure.feature('Авторизация')
class TestAuth:

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка авторизации')
    @pytest.mark.auth
    def test_auth(self, auth_endpoint):
        auth_endpoint.get_auth_token(test_data.login, test_data.password)