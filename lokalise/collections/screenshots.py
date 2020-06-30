"""
lokalise.collections.screenshots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing screenshots collection.
"""

from .base_collection import BaseCollection
from ..models.screenshot import ScreenshotModel


class ScreenshotsCollection(BaseCollection):
    """Describes screenshots.
    """
    DATA_KEY = "screenshots"
    MODEL_KLASS = ScreenshotModel
