import pytest
import allure

@allure.feature('Страница профилей')
class TestProfiles:

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка получения профиля')
    @pytest.mark.profiles
    def test_get_profile_by_id(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        profile_endpoint.get_profile_by_id(response)
        profile_endpoint.delete_profile(response)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка изменения профиля')
    @pytest.mark.profiles
    def test_put_profile_by_id(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        profile_endpoint.put_profile_by_id(response)
        profile_endpoint.delete_profile(response)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка удаления профиля')
    @pytest.mark.profiles
    def test_delete_profile(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        profile_endpoint.delete_profile(response)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка получения всех профилей')
    @pytest.mark.profiles
    def test_get_all_profiles(self, profile_endpoint):
        profile_endpoint.get_all_profiles()

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка создания профиля')
    @pytest.mark.profiles
    def test_create_new_profile(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        profile_endpoint.delete_profile(response)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка копирования профиля')
    @pytest.mark.profiles
    def test_copy_profile(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        new_response = profile_endpoint.copy_profile(response)
        profile_endpoint.delete_profile(response)
        profile_endpoint.delete_profile(new_response)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка получения активного профиля')
    @pytest.mark.profiles
    def test_get_active_profile(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        profile_endpoint.get_active_profile(response)
        profile_endpoint.delete_profile(response)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка активации профиля')
    @pytest.mark.profiles
    def test_activate_profile(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        profile_endpoint.activate_profile(response)
        profile_endpoint.delete_profile(response)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка деактивации профиля')
    @pytest.mark.profiles
    def test_deactivate_profile(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        profile_endpoint.deactivate_profile()
        profile_endpoint.delete_profile(response)
