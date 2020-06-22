"""
lokalise.models.file
~~~~~~~~~~~~~~~~~~~~~~~~
Module containing file model.
"""

from .base_model import BaseModel


class FileModel(BaseModel):
    """Describes file.
    """
    ATTRS = [
        'filename',
        'key_count'
    ]
