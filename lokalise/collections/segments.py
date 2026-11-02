"""
lokalise.collections.segments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing segments collection.
"""

from ..models.segment import SegmentModel
from .expert_collection import ExpertCollection


class SegmentsCollection(ExpertCollection[SegmentModel]):
    """Describes segments."""

    DATA_KEY = "segments"
    MODEL_KLASS = SegmentModel
