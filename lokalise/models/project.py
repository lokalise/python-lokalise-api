from .base_model import BaseModel


class ProjectModel(BaseModel):
    ATTRS = [
        "project_id",
        "project_type",
        "name",
        "description",
        "created_at",
        "created_at_timestamp",
        "created_by",
        "created_by_email",
        "team_id",
        "base_language_id",
        "base_language_iso",
        "settings",
        "statistics"
    ]
