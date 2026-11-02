"""
lokalise.collections.teams
~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing teams collection.
"""

from ..models.team import TeamModel
from .expert_collection import ExpertCollection


class TeamsCollection(ExpertCollection[TeamModel]):
    """Describes teams."""

    DATA_KEY = "teams"
    MODEL_KLASS = TeamModel
