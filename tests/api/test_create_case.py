import pytest
from utils.fake_data_provider import *
from dto.case_dto import CaseDTO, CaseData, CaseAttributes
from dto.suite_dto import SuiteDTO, SuiteData, SuiteAttributes
from controllers.case_controller import *
from controllers.suite_controller import *


class TestCreateCase:
    @pytest.fixture
    def case_dto(self, jwt_token):
        suite_title = "suite " + faker.word()
        suite_description = "suite desc " + faker.word() + " " + faker.word()
        suite_dto = SuiteDTO(
            data=SuiteData(
                id="api_tests",
                attributes=SuiteAttributes(
                    title=suite_title,
                    description=suite_description
                ),
                relationships={}
            )
        )
        test_suite_controller.create_test_suite(suite_dto, jwt_token)
        suite_id = test_suite_controller.get_suite_id_by_title(suite_title, jwt_token)

        case_title = "case " + faker.word()
        case_description = "case desc " + faker.word() + " " + faker.word()
        self.case_dto = CaseDTO(
            data=CaseData(
                id="api_tests",
                attributes=CaseAttributes.parse_obj({
                    "title": case_title,
                    "description": case_description,
                    "suite-id": suite_id,
                    "public-title": case_title
                }),
                relationships={}
            )
        )
        yield
        test_case_controller.delete_case_by_title(case_title, jwt_token)
        test_suite_controller.delete_suite_by_title(suite_title, jwt_token)

    @pytest.mark.usefixtures("case_dto")
    def test_create_test_case(self, jwt_token):
        response = test_case_controller.create_test_case(self.case_dto, jwt_token)
        assert response.status_code == 200, "Error while creating test case"
