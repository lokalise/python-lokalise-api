"""
lokalise.endpoints.permission_templates_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing permission templates endpoint.
"""
from .base_endpoint import BaseEndpoint


class PermissionTemplatesEndpoint(BaseEndpoint):
    """Describes permission templates endpoint.
    """
    PATH = "teams/$parent_id/roles"
