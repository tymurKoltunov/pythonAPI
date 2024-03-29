from pydantic import BaseModel, Field
from typing import Optional


class SuiteAttributes(BaseModel):
    title: str
    description: str
    emoji: Optional[str] = None
    code: Optional[str] = None
    sync: bool = True
    file_type: Optional[str] = Field('suite', alias="file-type")
    test_count: Optional[int] = Field(0, alias="test-count")
    filtered_tests: Optional[str] = Field(None, alias="filtered-tests")
    file: Optional[str] = None
    is_root: Optional[bool] = Field(True, alias="is-root")
    jira_issues: Optional[str] = Field(None, alias="jira-issues")


class SuiteRelationships(BaseModel):
    pass


class SuiteData(BaseModel):
    id: str
    type: str = "suite"
    attributes: SuiteAttributes
    relationships: SuiteRelationships


class SuiteDTO(BaseModel):
    data: SuiteData
