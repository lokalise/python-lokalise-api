from typing import TypedDict

from lokalise.models.base_model import BaseModel

class TeamQuota(TypedDict):
    users: int
    keys: int
    projects: int
    mau: int
    ai_words: int

class TeamModel(BaseModel):
    team_id: int
    name: str
    created_at: str
    created_at_timestamp: int
    plan: str
    quota_usage: TeamQuota
    quota_allowed: TeamQuota
