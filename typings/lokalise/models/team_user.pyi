from lokalise.models.base_model import BaseModel

class TeamUserModel(BaseModel):
    user_id: int
    email: str
    fullname: str
    created_at: str
    created_at_timestamp: int
    role: str
    uuid: str | None
