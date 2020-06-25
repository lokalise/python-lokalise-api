"""
lokalise.collections.webhooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing webhooks collection.
"""

from .base_collection import BaseCollection
from ..models.webhook import WebhookModel


class WebhooksCollection(BaseCollection):
    """Describes translations.
    """
    DATA_KEY = "webhooks"
    MODEL_KLASS = WebhookModel
