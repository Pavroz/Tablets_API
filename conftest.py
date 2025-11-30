import pytest

from endpoints.auth_endpoint import AuthEndpoint
import random
import string # Хранилище стринговых символов

from endpoints.member_endpoint import MemberEndpoint
from endpoints.profiles_endpoint import ProfileEndpoint

@pytest.fixture()
def auth_endpoint():
    return AuthEndpoint()

@pytest.fixture()
def profile_endpoint():
    return ProfileEndpoint()

@pytest.fixture()
def member_endpoint():
    return MemberEndpoint()

@pytest.fixture()
def random_string():
    return ''.join(random.choices(string.ascii_lowercase, k=10))
