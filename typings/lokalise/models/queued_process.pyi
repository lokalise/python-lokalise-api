from typing import Any

from lokalise.models.base_model import BaseModel

class QueuedProcessModel(BaseModel):
    process_id: str
    type: str
    status: str
    message: str
    created_by: str
    created_by_email: str
    created_at: str
    created_at_timestamp: int
    details: dict[str, Any]
