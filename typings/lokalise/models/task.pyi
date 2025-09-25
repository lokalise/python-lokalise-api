from typing import TypedDict

from lokalise.models.base_model import BaseModel

class LanguageAssigneeUser(TypedDict):
    user_id: str | int
    email: str
    fullname: str

class LanguageAssigneeGroup(TypedDict):
    id: str | int
    name: str

InitialTMLeverage = TypedDict(
    "InitialTMLeverage",
    {
        "0%+": int,
        "60%+": int,
        "75%+": int,
        "95%+": int,
        "100%": int,
    },
)

TMLeverageValue = TypedDict(
    "TMLeverageValue",
    {
        "0%+": int,
        "50%+": int,
        "75%+": int,
        "85%+": int,
        "95%+": int,
        "100%": int,
    },
)

class TMLeverage(TypedDict):
    status: str
    value: TMLeverageValue

class LanguageEntry(TypedDict):
    language_iso: str
    users: list[LanguageAssigneeUser]
    groups: list[LanguageAssigneeGroup]
    keys: list[str] | list[int]
    status: str
    progress: int
    initial_tm_leverage: InitialTMLeverage
    tm_leverage: TMLeverage
    keys_count: int
    words_count: int
    completed_at: str
    completed_at_timestamp: int
    completed_by: int
    completed_by_email: str

class TaskModel(BaseModel):
    task_id: int
    title: str
    description: str
    status: str
    progress: int
    due_date: str
    due_date_timestamp: int
    keys_count: int
    words_count: int
    created_at: str
    created_at_timestamp: int
    created_by: int
    created_by_email: str
    can_be_parent: bool
    task_type: str
    parent_task_id: int
    closing_tags: list[str]
    do_lock_translations: bool
    languages: list[LanguageEntry]
    source_language_iso: str
    auto_close_languages: bool
    auto_close_task: bool
    auto_close_items: bool
    completed_at: str
    completed_at_timestamp: int
    completed_by: int
    completed_by_email: str
    custom_translation_status_ids: list[int]
