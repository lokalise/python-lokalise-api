"""
lokalise.collections.webhooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing webhooks collection.
"""

from ..models.webhook import WebhookModel
from .expert_collection import ExpertCollection


class WebhooksCollection(ExpertCollection[WebhookModel]):
    """Describes webhooks."""

    DATA_KEY = "webhooks"
    MODEL_KLASS = WebhookModel
