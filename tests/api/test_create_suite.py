import pytest
from utils.fake_data_provider import *
from dto.suite_dto import SuiteDTO, SuiteData, SuiteAttributes
from controllers.suite_controller import TestSuiteController


class TestCreateSuite:
    @pytest.fixture
    def suite_dto(self, jwt_token):
        self.test_suite_controller = TestSuiteController().withJwtToken(jwt_token)
        title = faker.word()
        description = faker.word() + " " + faker.word()
        self.suite_dto = SuiteDTO(
            data=SuiteData(
                id="api_tests",
                attributes=SuiteAttributes(
                    title=title,
                    description=description
                ),
                relationships={}
            )
        )
        yield
        self.test_suite_controller.delete_suite_by_title(title)

    @pytest.mark.usefixtures("suite_dto")
    def test_create_suite(self, jwt_token):
        response = self.test_suite_controller.create_test_suite(self.suite_dto)
        assert response.status_code == 200, "Error while creating test suite"
