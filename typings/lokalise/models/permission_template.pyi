from lokalise.models.base_model import BaseModel

class PermissionTemplateModel(BaseModel):
    id: int
    role: str
    permissions: list[str]
    description: str
    tag: str
    tagColor: str
    tagInfo: str | None
    doesEnableAllReadOnlyLanguages: bool
