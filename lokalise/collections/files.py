"""
lokalise.collections.files
~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing files collection.
"""

from ..models.file import FileModel
from .base_collection import BaseCollection


class FilesCollection(BaseCollection[FileModel]):
    """Describes files."""

    DATA_KEY = "files"
    MODEL_KLASS = FileModel
