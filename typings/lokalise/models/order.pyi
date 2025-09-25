from typing import Any

from lokalise.models.base_model import BaseModel

class OrderModel(BaseModel):
    order_id: str
    project_id: str
    branch: str
    payment_method: str | None
    card_id: int | str
    status: str
    created_at: str
    created_at_timestamp: int
    created_by: int
    created_by_email: str
    source_language_iso: str
    target_language_isos: list[str]
    keys: list[int] | list[str]
    source_words: dict[str, Any]
    provider_slug: str
    translation_style: str
    translation_tier: int
    translation_tier_name: str
    briefing: str
    is_saved_to_translation_memory: bool
    total: int
    dry_run: bool
