"""
lokalise.collections.segments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing segments collection.
"""

from .base_collection import BaseCollection
from ..models.segment import SegmentModel


class SegmentsCollection(BaseCollection):
    """Describes segments.
    """
    DATA_KEY = "segments"
    MODEL_KLASS = SegmentModel
