import pytest

from controllers.auth_controller import AuthController


@pytest.fixture(scope="session")
def jwt_token():
    auth = AuthController()
    return auth.get_jwt_token()
