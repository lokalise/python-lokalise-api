"""
lokalise.collections.screenshots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing screenshots collection.
"""

from ..models.screenshot import ScreenshotModel
from .expert_collection import ExpertCollection


class ScreenshotsCollection(ExpertCollection[ScreenshotModel]):
    """Describes screenshots."""

    DATA_KEY = "screenshots"
    MODEL_KLASS = ScreenshotModel
