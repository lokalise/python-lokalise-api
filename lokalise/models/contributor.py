from .base_model import BaseModel


class ContributorModel(BaseModel):
    DATA_KEY = 'contributor'

    ATTRS = [
        "user_id",
        "email",
        "fullname",
        "created_at",
        "created_at_timestamp",
        "is_admin",
        "is_reviewer",
        "languages",
        "admin_rights",
    ]
