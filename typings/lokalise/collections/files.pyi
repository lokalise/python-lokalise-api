from lokalise.collections.base_collection import BaseCollection
from lokalise.models.file import FileModel

class FilesCollection(BaseCollection[FileModel]):
    items: list[FileModel]
