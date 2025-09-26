from typing import Any

from lokalise.models.base_model import BaseModel

class TeamUserGroupModel(BaseModel):
    group_id: int
    name: str
    permissions: dict[str, Any]
    created_at: str
    created_at_timestamp: int
    team_id: int
    projects: list[str] | list[int]
    members: list[int] | list[str]
    role_id: int | None
