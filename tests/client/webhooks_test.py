"""
Tests for the Webhooks endpoint.
"""

import pytest


PROJECT_ID = "454087345e09f3e7e7eae3.57891254"

@pytest.mark.vcr
def test_create_webhook(client):
    """Tests creation of a webhook
    """
    webhook = client.create_webhook(PROJECT_ID, {
        "url": r"http://bodrovis.tech/lokalise",
        "events": ["project.imported", "project.snapshot"]
    })
    assert webhook.project_id == PROJECT_ID
    assert "project.snapshot" in webhook.events
    assert "/lokalise" in webhook.url
