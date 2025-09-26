from typing import Any

from lokalise.models.base_model import BaseModel

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
    languages: list[dict[str, Any]]
    source_language_iso: str
    auto_close_languages: bool
    auto_close_task: bool
    auto_close_items: bool
    completed_at: str
    completed_at_timestamp: int
    completed_by: int
    completed_by_email: str
    custom_translation_status_ids: list[int]
