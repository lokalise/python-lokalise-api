from typing import TypedDict

from lokalise.models.base_model import BaseModel

class PermissionLanguage(TypedDict):
    lang_id: int
    lang_iso: str
    lang_name: str
    is_writable: bool

class GroupPermissions(TypedDict):
    is_admin: bool  # deprecated
    is_reviewer: bool  # deprecated
    admin_rights: list[str]
    languages: list[PermissionLanguage]

class TeamUserGroupModel(BaseModel):
    group_id: int
    name: str
    permissions: GroupPermissions
    created_at: str
    created_at_timestamp: int
    team_id: int
    projects: list[str] | list[int]
    members: list[int] | list[str]
    role_id: int | None
