"""
lokalise.collections.permission_templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing permission templates collection.
"""

from ..models.permission_template import PermissionTemplateModel
from .base_collection import BaseCollection


class PermissionTemplatesCollection(BaseCollection[PermissionTemplateModel]):
    """Describes permission templates."""

    DATA_KEY = "roles"
    MODEL_KLASS = PermissionTemplateModel
