"""
lokalise.collections.files
~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing files collection.
"""

from .base_collection import BaseCollection
from ..models.file import FileModel


class FilesCollection(BaseCollection):
    """Describes files.
    """
    DATA_KEY = "files"
    MODEL_KLASS = FileModel
