"""
lokalise.collections.files
~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing files collection.
"""

from ..models.file import FileModel
from .expert_collection import ExpertCollection


class FilesCollection(ExpertCollection[FileModel]):
    """Describes files."""

    DATA_KEY = "files"
    MODEL_KLASS = FileModel
