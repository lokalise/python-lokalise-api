"""
lokalise.collections.teams
~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing teams collection.
"""

from ..models.team import TeamModel
from .base_collection import BaseCollection


class TeamsCollection(BaseCollection[TeamModel]):
    """Describes teams."""

    DATA_KEY = "teams"
    MODEL_KLASS = TeamModel
