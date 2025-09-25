from lokalise.models.base_model import BaseModel

class BranchModel(BaseModel):
    branch_id: int
    name: str
    created_at: str
    created_at_timestamp: int
    created_by: int
    created_by_email: str
