"""
lokalise.models.glossary_term
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing glossary term model.
"""

from .base_model import BaseModel


class GlossaryTermModel(BaseModel):
    """Describes a glossary term."""

    DATA_KEY = "data"

    ATTRS = [
        "id",
        "projectId",
        "term",
        "description",
        "caseSensitive",
        "translatable",
        "forbidden",
        "translations",
        "tags",
        "createdAt",
        "updatedAt",
    ]
