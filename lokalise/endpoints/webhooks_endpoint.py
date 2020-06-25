"""
lokalise.endpoints.webhooks_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing webhooks endpoint.
"""
from .base_endpoint import BaseEndpoint


class WebhooksEndpoint(BaseEndpoint):
    """Describes webhooks endpoint.
    """
    PATH = "projects/$parent_id/webhooks/$resource_id"
