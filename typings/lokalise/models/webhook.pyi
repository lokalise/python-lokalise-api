from typing import TypedDict

from lokalise.models.base_model import BaseModel

class WebhookEventLangMap(TypedDict):
    event: str
    lang_iso_codes: list[str]

class WebhookModel(BaseModel):
    webhook_id: str
    url: str
    secret: str
    events: list[str]
    event_lang_map: list[WebhookEventLangMap]
