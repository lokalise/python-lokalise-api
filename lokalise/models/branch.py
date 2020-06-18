"""
lokalise.models.branch
~~~~~~~~~~~~~~~~~~~~~~
Module containing branch model.
"""
from .base_model import BaseModel


class BranchModel(BaseModel):
    """Describes project branch model.
    """
    DATA_KEY = 'branch'

    ATTRS = [
        'branch_id',
        'name',
        'created_at',
        'created_at_timestamp',
        'created_by',
        'created_by_email'
    ]
