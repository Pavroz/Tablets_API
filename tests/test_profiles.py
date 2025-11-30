from data import test_data
import pytest
import allure

@allure.feature('Страница профилей')
class TestProfiles:

    def test_get_profile_by_id(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        profile_endpoint.get_profile_by_id(response)
        profile_endpoint.delete_profile(response)

    def test_put_profile_by_id(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        profile_endpoint.put_profile_by_id(response)
        profile_endpoint.delete_profile(response)

    def test_delete_profile(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        profile_endpoint.delete_profile(response)

    def test_get_all_profiles(self, profile_endpoint):
        profile_endpoint.get_all_profiles()

    def test_create_new_profile(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        profile_endpoint.delete_profile(response)

    def test_copy_profile(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        new_response = profile_endpoint.copy_profile(response)
        profile_endpoint.delete_profile(response)
        profile_endpoint.delete_profile(new_response)

    def test_get_active_profile(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        profile_endpoint.get_active_profile(response)
        profile_endpoint.delete_profile(response)

    def test_activate_profile(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        profile_endpoint.activate_profile(response)
        profile_endpoint.delete_profile(response)

    def test_deactivate_profile(self, profile_endpoint):
        response = profile_endpoint.create_new_profile()
        profile_endpoint.deactivate_profile(response)
        profile_endpoint.delete_profile(response)
