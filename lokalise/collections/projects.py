"""
lokalise.collections.projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing projects collection.
"""

from ..models.project import ProjectModel
from .expert_collection import ExpertCollection


class ProjectsCollection(ExpertCollection[ProjectModel]):
    """Describes projects."""

    DATA_KEY = "projects"
    MODEL_KLASS = ProjectModel
