from lokalise.models.base_model import BaseModel

class FileModel(BaseModel):
    file_id: int
    filename: str
    key_count: int
