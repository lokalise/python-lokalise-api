"""
lokalise.endpoints.project_comments_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing project comments endpoint.
"""

from .base_endpoint import BaseEndpoint


class ProjectCommentsEndpoint(BaseEndpoint):
    """Describes project comments endpoint."""

    PATH = "projects/$parent_id/comments"
