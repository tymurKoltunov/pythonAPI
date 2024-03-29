import pytest
from controllers.url_controller import *


@pytest.fixture(scope="session")
def jwt_token():
    return get_jwt_token()
