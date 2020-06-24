"""
lokalise.endpoints.tasks_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing tasks endpoint.
"""
from .base_endpoint import BaseEndpoint


class TasksEndpoint(BaseEndpoint):
    """Describes tasks endpoint.
    """
    PATH = "projects/$parent_id/tasks/$resource_id"
