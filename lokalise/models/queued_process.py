"""
lokalise.models.queued_process
~~~~~~~~~~~~~~~~~~~~~~~~
Module containing queued process model.
"""

from .base_model import BaseModel


class QueuedProcessModel(BaseModel):
    """Describes queued process.
    """
    DATA_KEY = 'process'

    ATTRS = [
        'process_id',
        'type',
        'status',
        'message',
        'created_by',
        'created_by_email',
        'created_at',
        'created_at_timestamp',
        'details'
    ]
