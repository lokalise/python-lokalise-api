"""
lokalise.collections.permission_templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing permission templates collection.
"""

from .base_collection import BaseCollection
from ..models.permission_template import PermissionTemplateModel


class PermissionTemplatesCollection(BaseCollection):
    """Describes permission templates.
    """
    DATA_KEY = "roles"
    MODEL_KLASS = PermissionTemplateModel
