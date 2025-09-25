from lokalise.models.base_model import BaseModel
from typing import Any

class ProjectModel(BaseModel):
    project_id: str
    project_type: str
    uuid: str | None
    name: str
    description: str
    created_at: str
    created_at_timestamp: int
    created_by: int
    created_by_email: str
    team_id: int
    team_uuid: str
    base_language_id: int
    base_language_iso: str
    settings: dict[str, Any]
    statistics: dict[str, Any]
