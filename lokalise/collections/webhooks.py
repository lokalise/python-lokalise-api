"""
lokalise.collections.webhooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing webhooks collection.
"""

from .base_collection import BaseCollection
from ..models.webhook import WebhookModel


class WebhooksCollection(BaseCollection):
    """Describes webhooks.
    """
    DATA_KEY = "webhooks"
    MODEL_KLASS = WebhookModel
