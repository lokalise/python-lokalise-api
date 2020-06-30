"""
lokalise.endpoints.snapshots_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing snapshots endpoint.
"""
from .base_endpoint import BaseEndpoint


class SnapshotsEndpoint(BaseEndpoint):
    """Describes snapshots endpoint.
    """
    PATH = "projects/$parent_id/snapshots/$resource_id"
