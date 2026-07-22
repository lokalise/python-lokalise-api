"""
lokalise.endpoints.audit_logs_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing audit logs endpoint.
"""

from ..base_endpoint import BaseEndpoint


class AuditLogsEndpoint(BaseEndpoint):
    """Describes audit logs endpoint."""

    PATH = "audit-logs"
