"""
lokalise.collections.screenshots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing screenshots collection.
"""

from ..models.screenshot import ScreenshotModel
from .base_collection import BaseCollection


class ScreenshotsCollection(BaseCollection[ScreenshotModel]):
    """Describes screenshots."""

    DATA_KEY = "screenshots"
    MODEL_KLASS = ScreenshotModel
