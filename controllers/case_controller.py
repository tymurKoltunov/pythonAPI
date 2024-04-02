import json

import requests
from controllers.base_controller import *


class TestCaseController(BaseController):

    def __init__(self, project_id=BaseController.PROJECT_ID):
        self.project_id = project_id

    def get_base_api_url(self):
        return super().get_base_api_url() + self.project_id + self.TESTS

    def create_test_case(self, case_dto):
        response = requests.post(self.get_base_api_url(),
                                 headers={"Authorization": self.TOKEN},
                                 json=case_dto.model_dump())
        return response

    def get_case_id_by_title(self, title):
        response = requests.get(self.get_base_api_url(),
                                headers={"Authorization": self.TOKEN})
        content = json.loads(response.content)
        for case in content["data"]:
            if case["attributes"]["title"] == title:
                return case["id"]

    def delete_case_by_title(self, title):
        case_id = self.get_case_id_by_title(title)
        requests.delete(self.get_base_api_url() + f"/{case_id}",
                        headers={"Authorization": self.TOKEN})


