"""
lokalise.models.order
~~~~~~~~~~~~~~~~~~~~~
Module containing order model.
"""

from .base_model import BaseModel


class OrderModel(BaseModel):
    """Describes order."""

    ATTRS = [
        "order_id",
        "project_id",
        "branch",
        "card_id",
        "status",
        "created_at",
        "created_at_timestamp",
        "created_by",
        "created_by_email",
        "source_language_iso",
        "target_language_isos",
        "keys",
        "source_words",
        "provider_slug",
        "translation_style",
        "translation_tier",
        "translation_tier_name",
        "briefing",
        "total",
        "dry_run",
        "payment_method",
        "is_saved_to_translation_memory",
    ]
