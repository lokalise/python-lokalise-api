from typing import Any

from lokalise.models.base_model import BaseModel

class GlossaryTermModel(BaseModel):
    id: int
    projectId: str
    term: str
    description: str
    caseSensitive: bool
    translatable: bool
    forbidden: bool
    translations: list[dict[str, Any]]
    tags: list[str]
    createdAt: str
    updatedAt: str | None
