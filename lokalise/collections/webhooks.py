"""
lokalise.collections.webhooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing webhooks collection.
"""

from ..models.webhook import WebhookModel
from .base_collection import BaseCollection


class WebhooksCollection(BaseCollection[WebhookModel]):
    """Describes webhooks."""

    DATA_KEY = "webhooks"
    MODEL_KLASS = WebhookModel
