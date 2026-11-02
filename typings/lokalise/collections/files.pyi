from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.file import FileModel

class FilesCollection(ExpertCollection[FileModel]):
    items: list[FileModel]
