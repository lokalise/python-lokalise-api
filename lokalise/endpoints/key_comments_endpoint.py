"""
lokalise.endpoints.key_comments_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing key comments endpoint.
"""
from .base_endpoint import BaseEndpoint


class KeyCommentsEndpoint(BaseEndpoint):
    """Describes key comments endpoint.
    """
    PATH = "projects/{project_id}/keys/{resource_id}/comments"
