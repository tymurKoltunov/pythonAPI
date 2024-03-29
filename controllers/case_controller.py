import requests
from controllers.url_controller import *
from utils.urls import URL


class TestCaseController:
    def create_test_case(self, case_dto, token):
        response = requests.post(get_base_api_url() + URL.project_id.value + URL.tests.value,
                                 headers={"Authorization": token},
                                 json=case_dto.model_dump())
        return response

    def get_case_id_by_title(self, title, token):
        response = requests.get(get_base_api_url() + URL.project_id.value + URL.suites.value,
                                headers={"Authorization": token})
        content = json.loads(response.content)
        for case in content["data"]:
            if case["attributes"]["title"] == title:
                return case["id"]

    def delete_case_by_title(self, title, token):
        case_id = self.get_case_id_by_title(title, token)
        requests.delete(get_base_api_url() + URL.project_id.value + URL.tests.value + f"/{case_id}",
                        headers={"Authorization": token})


test_case_controller = TestCaseController()
