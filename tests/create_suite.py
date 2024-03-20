from dto.test_suite import TestSuiteDTO, Data, Attributes
from controllers.test_suite_controller import *


def test_create_test_suite():
    suite_dto = TestSuiteDTO(
        data=Data(
            id="api_tests",
            type="suite",
            attributes=Attributes(
                title="first",
                description="first description",
                emoji=None,
                code=None,
                sync=True,
                file_type="suite",
                test_count=0,
                filtered_tests=None,
                file=None,
                is_root=True,
                jira_issues=None
            ),
            relationships={}
        )
    )

    response = create_test_suite(suite_dto)
    assert response.status_code == 200
