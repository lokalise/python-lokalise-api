from lokalise.models.project import ProjectModel
from lokalise.collections.base_collection import BaseCollection

class ProjectsCollection(BaseCollection[ProjectModel]):
    items: list[ProjectModel]
