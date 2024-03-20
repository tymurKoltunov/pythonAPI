import requests
from controllers.url_controller import *
from utils.urls import URL


def create_test_suite(suite_dto):
    response = requests.post(get_base_api_url() + URL.projects.value, headers={"Authorization": get_jwt_token()},
                             json=suite_dto.dict())
    return response
