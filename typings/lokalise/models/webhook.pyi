from typing import Any

from lokalise.models.base_model import BaseModel

class WebhookModel(BaseModel):
    webhook_id: str
    url: str
    secret: str
    events: list[str]
    event_lang_map: list[dict[str, Any]]
