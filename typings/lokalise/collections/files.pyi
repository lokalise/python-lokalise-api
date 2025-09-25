from lokalise.models.file import FileModel
from lokalise.collections.base_collection import BaseCollection

class FilesCollection(BaseCollection[FileModel]):
    items: list[FileModel]
