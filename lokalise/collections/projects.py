"""
lokalise.collections.projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing projects collection.
"""

from ..models.project import ProjectModel
from .base_collection import BaseCollection


class ProjectsCollection(BaseCollection[ProjectModel]):
    """Describes projects."""

    DATA_KEY = "projects"
    MODEL_KLASS = ProjectModel
