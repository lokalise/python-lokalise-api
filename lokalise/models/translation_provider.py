"""
lokalise.models.translation_provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translation provider model.
"""

from .base_model import BaseModel


class TranslationProviderModel(BaseModel):
    """Describes translation provider model.
    """
    ATTRS = [
        'provider_id',
        'name',
        'slug',
        'price_pair_min',
        'website_url',
        'description',
        'tiers',
        'pairs'
    ]
