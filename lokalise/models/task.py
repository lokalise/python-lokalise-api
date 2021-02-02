"""
lokalise.models.task
~~~~~~~~~~~~~~~~~~~~
Module containing task model.
"""

from .base_model import BaseModel


class TaskModel(BaseModel):
    """Describes a task.
    """
    DATA_KEY = 'task'

    ATTRS = [
        'task_id',
        'title',
        'description',
        'status',
        'progress',
        'due_date',
        'due_date_timestamp',
        'keys_count',
        'words_count',
        'created_at',
        'created_at_timestamp',
        'created_by',
        'created_by_email',
        'can_be_parent',
        'task_type',
        'parent_task_id',
        'closing_tags',
        'do_lock_translations',
        'languages',
        'auto_close_languages',
        'auto_close_task',
        'auto_close_items',
        'completed_at',
        'completed_at_timestamp',
        'completed_by',
        'completed_by_email',
        'custom_translation_status_ids'
    ]
