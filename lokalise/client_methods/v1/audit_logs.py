"""
lokalise.client_methods.audit_logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for audit logs.
"""

from typing import Any

from lokalise.collections.v1.audit_logs import AuditLogsCollection

from ..endpoint_provider import EndpointProviderMixin


class AuditLogsMethods(EndpointProviderMixin):
    """Audit logs client methods."""

    def audit_logs(self, params: dict[str, Any] | None = None) -> AuditLogsCollection:
        """Fetches audit logs.

        :param dict params: Request parameters
        :return: Collection of audit logs
        """
        raw_audit_logs = self.get_endpoint("audit_logs", namespace="v1").all(params=params)
        return AuditLogsCollection(raw_audit_logs)
