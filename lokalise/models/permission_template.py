"""
lokalise.models.permission_template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing permission template.
"""

from .base_model import BaseModel


class PermissionTemplateModel(BaseModel):
    """Describes permission template."""

    ATTRS = [
        "id",
        "role",
        "permissions",
        "description",
        "tag",
        "tagColor",
        "tagInfo",
        "doesEnableAllReadOnlyLanguages",
    ]
