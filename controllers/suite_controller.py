import json

import requests
from controllers.base_controller import *


class TestSuiteController(BaseController):
    def __init__(self, project_id=BaseController.PROJECT_ID):
        self.project_id = project_id

    def get_base_api_url(self):
        return super().get_base_api_url() + self.project_id + self.SUITES

    def create_test_suite(self, suite_dto):
        response = requests.post(self.get_base_api_url(),
                                 headers={"Authorization": self.TOKEN},
                                 json=suite_dto.model_dump())
        return response

    def get_suite_id_by_title(self, title):
        response = requests.get(self.get_base_api_url(),
                                headers={"Authorization": self.TOKEN})
        content = json.loads(response.content)
        for suite in content["data"]:
            if suite["attributes"]["title"] == title:
                return suite["id"]

    def delete_suite_by_title(self, title):
        suite_id = self.get_suite_id_by_title(title)
        requests.delete(self.get_base_api_url() + f"/{suite_id}",
                        headers={"Authorization": self.TOKEN})


