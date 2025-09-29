"""
lokalise.collections.segments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing segments collection.
"""

from ..models.segment import SegmentModel
from .base_collection import BaseCollection


class SegmentsCollection(BaseCollection[SegmentModel]):
    """Describes segments."""

    DATA_KEY = "segments"
    MODEL_KLASS = SegmentModel
