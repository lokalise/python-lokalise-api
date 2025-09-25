from typing import TypedDict

from lokalise.models.base_model import BaseModel

class TranslationStatusModel(BaseModel):
    status_id: int
    title: str
    color: str

class TranslationStatusDict(TypedDict):
    status_id: int
    title: str
    color: str
