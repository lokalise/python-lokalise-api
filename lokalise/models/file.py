"""
lokalise.models.file
~~~~~~~~~~~~~~~~~~~~
Module containing file model.
"""

from .base_model import BaseModel


class FileModel(BaseModel):
    """Describes file."""

    ATTRS = ["file_id", "filename", "key_count"]
