from typing import Any

from lokalise.models.base_model import BaseModel

class TeamModel(BaseModel):
    team_id: int
    name: str
    created_at: str
    created_at_timestamp: int
    plan: str
    quota_usage: dict[str, Any]
    quota_allowed: dict[str, Any]
