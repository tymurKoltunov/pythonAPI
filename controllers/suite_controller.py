import requests
from controllers.url_controller import *
from utils.urls import URL


class TestSuiteController:
    def create_test_suite(self, suite_dto, token):
        response = requests.post(get_base_api_url() + URL.project_id.value + URL.suites.value,
                                 headers={"Authorization": token},
                                 json=suite_dto.model_dump())
        return response

    def get_suite_id_by_title(self, title, token):
        response = requests.get(get_base_api_url() + URL.project_id.value + URL.suites.value,
                                headers={"Authorization": token})
        content = json.loads(response.content)
        for suite in content["data"]:
            if suite["attributes"]["title"] == title:
                return suite["id"]

    def delete_suite_by_title(self, title, token):
        suite_id = self.get_suite_id_by_title(title, token)
        requests.delete(get_base_api_url() + URL.project_id.value + URL.suites.value + f"/{suite_id}",
                        headers={"Authorization": token})


test_suite_controller = TestSuiteController()
