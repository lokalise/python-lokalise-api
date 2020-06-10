"""
lokalise.endpoints.projects_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing projects endpoint.
"""

from .base_endpoint import BaseEndpoint


class ProjectsEndpoint(BaseEndpoint):
    """Describes projects endpoint.
    """
    PATH = "projects/{project_id}"
