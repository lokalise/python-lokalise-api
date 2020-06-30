"""
lokalise.collections.teams
~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing teams collection.
"""

from .base_collection import BaseCollection
from ..models.team import TeamModel


class TeamsCollection(BaseCollection):
    """Describes teams.
    """
    DATA_KEY = "teams"
    MODEL_KLASS = TeamModel
