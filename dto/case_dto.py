from pydantic import BaseModel, Field
from typing import Optional, List


class CaseAttributes(BaseModel):
    title: str
    state: Optional[str] = None
    emoji: Optional[str] = None
    recordings_count: Optional[int] = Field(None, alias="recordings-count")
    code: Optional[str] = None
    file: Optional[str] = None
    priority: str = "normal"
    sync: bool = True
    last_sync_id: Optional[str] = Field(None, alias="last-sync-id")
    run_statuses: List[str] = Field(default_factory=list, alias="run-statuses")
    assigned_to: Optional[str] = Field(None, alias="assigned-to")
    description: str
    suite_id: str = Field(..., alias="suite-id")
    has_examples: Optional[bool] = Field(None, alias="has-examples")
    params: List[str] = Field(default_factory=list)
    public_title: str = Field(..., alias="public-title")
    tags: List[str] = Field(default_factory=list)
    previous_description: Optional[str] = Field(None, alias="previous-description")
    import_id: Optional[str] = Field(None, alias="import-id")
    play_url: Optional[str] = Field(None, alias="play-url")
    jira_issues: Optional[str] = Field(None, alias="jira-issues")
    attachments: Optional[str] = None


class CaseRelationships(BaseModel):
    pass


class CaseData(BaseModel):
    id: str
    type: str = "test"
    attributes: CaseAttributes
    relationships: CaseRelationships


class CaseDTO(BaseModel):
    data: CaseData
