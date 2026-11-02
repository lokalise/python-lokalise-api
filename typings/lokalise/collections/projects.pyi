from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.project import ProjectModel

class ProjectsCollection(ExpertCollection[ProjectModel]):
    items: list[ProjectModel]
