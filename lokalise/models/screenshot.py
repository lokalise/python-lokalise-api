"""
lokalise.models.screenshot
~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing screenshot model.
"""

from .base_model import BaseModel


class ScreenshotModel(BaseModel):
    """Describes screenshot."""

    DATA_KEY = "screenshot"

    ATTRS = [
        "screenshot_id",
        "key_ids",
        "keys",
        "url",
        "title",
        "description",
        "screenshot_tags",
        "width",
        "height",
        "created_at",
        "created_at_timestamp",
    ]
