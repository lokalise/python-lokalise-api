from lokalise.collections.base_collection import BaseCollection
from lokalise.models.project import ProjectModel

class ProjectsCollection(BaseCollection[ProjectModel]):
    items: list[ProjectModel]
