from lokalise.models.base_model import BaseModel

class CommentModel(BaseModel):
    comment_id: int
    key_id: int
    comment: str
    added_by: int
    added_by_email: str
    added_at: str
    added_at_timestamp: int
