"""
Tests for the Translation statuses endpoint.
"""

import pytest
from lokalise.client import Client

PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
STATUS_ID = 429
NEW_STATUS_ID = 1357


@pytest.mark.vcr
def test_translation_statuses(client: Client) -> None:
    """Tests fetching of all translation statuses"""
    statuses = client.translation_statuses(PROJECT_ID)
    assert statuses.project_id == PROJECT_ID
    assert statuses.items[0].title == "needs context"


@pytest.mark.vcr
def test_translation_statuses_pagination(client: Client) -> None:
    """Tests fetching of translation statuses with pagination"""
    statuses = client.translation_statuses(PROJECT_ID, {"page": 2, "limit": 1})
    assert statuses.project_id == PROJECT_ID
    assert statuses.items[0].title == "waiting for approval by director"
    assert statuses.current_page == 2
    assert statuses.total_count == 2
    assert statuses.page_count == 2
    assert statuses.limit == 1

    assert statuses.is_last_page()
    assert not statuses.is_first_page()
    assert not statuses.has_next_page()
    assert statuses.has_prev_page()


@pytest.mark.vcr
def test_translation_status(client: Client) -> None:
    """Tests fetching of a translation status"""
    status = client.translation_status(PROJECT_ID, STATUS_ID)
    assert status.project_id == PROJECT_ID
    assert status.status_id == STATUS_ID
    assert status.title == "needs context"
    assert status.color == "#61bd4f"


@pytest.mark.vcr
def test_create_translation_status(client: Client) -> None:
    """Tests creation of a translation status"""
    status = client.create_translation_status(
        PROJECT_ID, {"title": "Python status", "color": "#ff9f1a"}
    )
    assert status.project_id == PROJECT_ID
    assert status.status_id == NEW_STATUS_ID
    assert status.title == "Python status"
    assert status.color == "#ff9f1a"


@pytest.mark.vcr
def test_update_translation_status(client: Client) -> None:
    """Tests updating of a translation status"""
    status = client.update_translation_status(
        PROJECT_ID, NEW_STATUS_ID, {"title": "Python status updated"}
    )
    assert status.project_id == PROJECT_ID
    assert status.status_id == NEW_STATUS_ID
    assert status.title == "Python status updated"


@pytest.mark.vcr
def test_delete_translation_status(client: Client) -> None:
    """Tests deletion of a translation status"""
    resp = client.delete_translation_status(PROJECT_ID, NEW_STATUS_ID)
    assert resp["project_id"] == PROJECT_ID
    assert resp["custom_translation_status_deleted"]


@pytest.mark.vcr
def test_translation_statuses_colors(client: Client) -> None:
    """Tests fetching of available status colors"""
    colors = client.translation_statuses_colors(PROJECT_ID)
    assert "#61bd4f" in colors
