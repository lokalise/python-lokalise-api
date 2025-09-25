"""
lokalise.endpoints.queued_processes_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing queued processes endpoint.
"""

from .base_endpoint import BaseEndpoint


class QueuedProcessesEndpoint(BaseEndpoint):
    """Describes queued processes endpoint."""

    PATH = "projects/$parent_id/processes/$resource_id"
