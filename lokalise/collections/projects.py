from .base_collection import BaseCollection
from ..models.project import ProjectModel


class ProjectsCollection(BaseCollection):
    DATA_KEY = "projects"
    MODEL_KLASS = ProjectModel
