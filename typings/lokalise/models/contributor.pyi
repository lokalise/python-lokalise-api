from typing import Any

from lokalise.models.base_model import BaseModel

class ContributorModel(BaseModel):
    user_id: int
    email: str
    fullname: str
    created_at: str
    created_at_timestamp: int
    is_admin: bool  # deprecated
    is_reviewer: bool  # deprecated
    languages: list[dict[str, Any]]
    admin_rights: list[str]
    role_id: int
    uuid: str | None
