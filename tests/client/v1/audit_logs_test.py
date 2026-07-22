"""
Tests for the Audit logs endpoint.
"""

import pytest
from lokalise.client_v1 import ClientV1
from lokalise.errors import BadRequest


@pytest.mark.vcr
def test_audit_logs(clientv1: ClientV1) -> None:
    """Tests fetching audit logs without parameters."""
    audit_logs = clientv1.audit_logs()

    assert len(audit_logs) > 0

    iterated_audit_logs = list(audit_logs)
    assert iterated_audit_logs == audit_logs.items
    assert len(iterated_audit_logs) == len(audit_logs)

    audit_log = audit_logs[0]

    assert audit_log.class_uid == 6003
    assert audit_log.class_name == "API Activity"
    assert audit_log.category_uid == 6
    assert audit_log.category_name == "Application Activity"
    assert audit_log.activity_id == 99
    assert audit_log.activity_name == "Other"
    assert audit_log.type_uid == 600399
    assert audit_log.type_name is None
    assert audit_log.severity_id == 1
    assert audit_log.severity == "Informational"
    assert audit_log.status_id == 1
    assert audit_log.status == "Success"
    assert audit_log.time == 1753267304

    assert audit_log.metadata["event_code"] == "project.deleted"
    assert audit_log.metadata["version"] == "1.3.0"

    actor = audit_log.actor
    assert actor is not None
    assert actor["user"]["uid"] == "20181"

    src_endpoint = audit_log.src_endpoint
    assert src_endpoint is not None
    assert src_endpoint["ip"] == "1.1.1.1"

    http_request = audit_log.http_request
    assert http_request is not None
    assert http_request["url"]["url_string"] == ("https://app.lokalise.com/project/delete")

    enrichments = audit_log.enrichments
    assert enrichments is not None
    assert enrichments[0]["name"] == "team"
    assert enrichments[1]["name"] == "project"

    unmapped = audit_log.unmapped
    assert unmapped is not None
    assert unmapped["event_type_id"] == 1006

    assert audit_logs.has_more
    assert audit_logs.next_cursor is not None
    assert audit_logs.has_next_cursor()
    assert not audit_logs.is_last_page()


@pytest.mark.vcr
def test_audit_logs_with_params(clientv1: ClientV1) -> None:
    """Tests fetching audit logs with query parameters."""
    audit_logs = clientv1.audit_logs(
        {
            "limit": 1,
        }
    )

    assert len(audit_logs) == 1

    audit_log = audit_logs[0]

    assert audit_log.class_uid == 6003
    assert audit_log.class_name == "API Activity"
    assert audit_log.metadata["event_code"] == "project.deleted"
    assert audit_log.time == 1753267304

    assert audit_logs.has_more
    assert audit_logs.next_cursor is not None
    assert audit_logs.has_next_cursor()
    assert not audit_logs.is_last_page()


@pytest.mark.vcr
def test_audit_logs_with_invalid_cursor(clientv1: ClientV1) -> None:
    """Tests handling of an invalid audit logs cursor."""
    with pytest.raises(BadRequest) as exc_info:
        clientv1.audit_logs(
            {
                "cursor": "invalid-cursor",
            }
        )

    error = exc_info.value

    assert error.status_code == 400
    assert error.raw_text is not None
    assert "Unexpected response status: 400" in error.raw_text
