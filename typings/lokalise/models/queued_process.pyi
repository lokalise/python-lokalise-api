from typing import TypedDict

from typing_extensions import NotRequired

from lokalise.models.base_model import BaseModel

class _UploadedFile(TypedDict):
    status: str
    message: str
    name_original: str
    word_count_total: int
    key_count_total: int
    key_count_inserted: int
    key_count_updated: int
    key_count_skipped: int
    name_custom: NotRequired[str]

class UploadedFileProcessDetails(TypedDict):
    files: list[_UploadedFile]

class DownloadedFileProcessDetails(TypedDict):
    download_url: str
    file_size_kb: int
    total_number_of_keys: int

QueuedProcessDetails = UploadedFileProcessDetails | DownloadedFileProcessDetails

class QueuedProcessModel(BaseModel):
    process_id: str
    type: str
    status: str
    message: str
    created_by: str
    created_by_email: str
    created_at: str
    created_at_timestamp: int
    details: QueuedProcessDetails
