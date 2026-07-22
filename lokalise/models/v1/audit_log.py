"""
lokalise.models.audit_log
~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing audit log.
"""

from ..base_model import BaseModel


class AuditLogModel(BaseModel):
    """Describes audit log model."""

    ATTRS = [
        "class_uid",
        "class_name",
        "category_uid",
        "category_name",
        "activity_id",
        "activity_name",
        "type_uid",
        "type_name",
        "severity_id",
        "severity",
        "status_id",
        "status",
        "time",
        "metadata",
        "actor",
        "src_endpoint",
        "http_request",
        "enrichments",
        "unmapped",
    ]
