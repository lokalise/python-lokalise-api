"""
lokalise.collections.audit_logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing audit logs collection.
"""

from lokalise.models.v1.audit_log import AuditLogModel

from .base_collection import BaseCollectionV1


class AuditLogsCollection(BaseCollectionV1[AuditLogModel]):
    """Describes audit logs."""

    DATA_KEY = "data"
    MODEL_KLASS = AuditLogModel
