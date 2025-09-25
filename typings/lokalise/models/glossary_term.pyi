from lokalise.models.base_model import BaseModel

class GlossaryTermModel(BaseModel):
    id: int
    projectId: str
    term: str
    description: str
    caseSensitive: bool
    translatable: bool
    forbidden: bool

    class Translation(BaseModel):
        langId: int
        langName: str
        langIso: str
        translation: str
        description: str

    translations: list[Translation]
    tags: list[str]
    createdAt: str
    updatedAt: str | None
