"""
Tests for the Webhooks endpoint.
"""

import pytest


PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
WEBHOOK_ID = "0efe309ba1c83f966ab3c76b05d25f62fc67cd7d"
ANOTHER_WEBHOOK_ID = "b5873ff8a70084e98ef8b0d3f40335fe75d44046"

@pytest.mark.vcr
def test_webhooks(client):
    """Tests fetching of all webhooks
    """
    webhooks = client.webhooks(PROJECT_ID)
    assert webhooks.project_id == PROJECT_ID
    assert webhooks.items[0].webhook_id == ANOTHER_WEBHOOK_ID


@pytest.mark.vcr
def test_webhooks_pagination(client):
    """Tests fetching of all webhooks with pagination
    """
    webhooks = client.webhooks(PROJECT_ID, {"page": 2, "limit": 2})
    assert webhooks.project_id == PROJECT_ID
    assert webhooks.items[0].webhook_id == WEBHOOK_ID
    assert webhooks.current_page == 2
    assert webhooks.total_count == 3
    assert webhooks.page_count == 2
    assert webhooks.limit == 2

    assert webhooks.is_last_page()
    assert not webhooks.is_first_page()
    assert not webhooks.has_next_page()
    assert webhooks.has_prev_page()


@pytest.mark.vcr
def test_webhook(client):
    """Tests fetching of a webhook
    """
    webhook = client.webhook(PROJECT_ID, WEBHOOK_ID)
    assert webhook.project_id == PROJECT_ID
    assert webhook.webhook_id == WEBHOOK_ID
    assert 'lokalise' in webhook.url
    assert 'a7ea7' in webhook.secret
    assert "project.branch.added" in webhook.events
    assert webhook.event_lang_map == []


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


@pytest.mark.vcr
def test_update_webhook(client):
    """Tests updating of a webhook
    """
    webhook = client.update_webhook(PROJECT_ID, WEBHOOK_ID, {
        "events": ["project.translation.updated"]
    })
    assert webhook.project_id == PROJECT_ID
    assert webhook.webhook_id == WEBHOOK_ID
    assert "project.translation.updated" in webhook.events


@pytest.mark.vcr
def test_delete_webhook(client):
    """Tests deletion of a webhook
    """
    resp = client.delete_webhook(PROJECT_ID, WEBHOOK_ID)
    assert resp['project_id'] == PROJECT_ID
    assert resp['webhook_deleted']


@pytest.mark.vcr
def test_regenerate_webhook_secret(client):
    """Tests regeneration of a webhook secret
    """
    resp = client.regenerate_webhook_secret(PROJECT_ID, ANOTHER_WEBHOOK_ID)
    assert resp['project_id'] == PROJECT_ID
    assert "9c7cc" in resp['secret']
