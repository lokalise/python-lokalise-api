"""
lokalise.models.audit_log
~~~~~~~~~~~~~~~~~~~~~~~~~
Type definitions for the audit log model.
"""

from typing import Any

from lokalise.models.base_model import BaseModel

class AuditLogModel(BaseModel):
    class_uid: int
    class_name: str | None

    category_uid: int
    category_name: str | None

    activity_id: int
    activity_name: str | None

    type_uid: int
    type_name: str | None

    severity_id: int
    severity: str | None

    status_id: int | None
    status: str | None

    time: int

    metadata: dict[str, Any]
    actor: dict[str, Any] | None
    src_endpoint: dict[str, Any] | None
    http_request: dict[str, Any] | None
    enrichments: list[dict[str, Any]] | None
    unmapped: dict[str, Any] | None
