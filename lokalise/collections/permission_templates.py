"""
lokalise.collections.permission_templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing permission templates collection.
"""

from ..models.permission_template import PermissionTemplateModel
from .expert_collection import ExpertCollection


class PermissionTemplatesCollection(ExpertCollection[PermissionTemplateModel]):
    """Describes permission templates."""

    DATA_KEY = "roles"
    MODEL_KLASS = PermissionTemplateModel
