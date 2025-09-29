from lokalise.models.base_model import BaseModel

class SnapshotModel(BaseModel):
    snapshot_id: int
    title: str
    created_at: str
    created_at_timestamp: int
    created_by: int
    created_by_email: str
