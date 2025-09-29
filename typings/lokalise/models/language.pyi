from lokalise.models.base_model import BaseModel

class LanguageModel(BaseModel):
    lang_id: int
    lang_iso: str
    lang_name: str
    is_rtl: bool
    plural_forms: list[str]
    project_language_uuid: str | None
