"""
lokalise.models.webhook
~~~~~~~~~~~~~~~~~~~~~~~
Module containing webhook model.
"""

from .base_model import BaseModel


class WebhookModel(BaseModel):
    """Describes webhook model."""

    DATA_KEY = "webhook"

    ATTRS = ["webhook_id", "url", "secret", "events", "event_lang_map"]
