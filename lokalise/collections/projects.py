"""
lokalise.collections.projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing projects collection.
"""

from .base_collection import BaseCollection
from ..models.project import ProjectModel


class ProjectsCollection(BaseCollection):
    """Describes projects.
    """
    DATA_KEY = "projects"
    MODEL_KLASS = ProjectModel
