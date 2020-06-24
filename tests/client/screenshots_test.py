"""
Tests for the Screenshots endpoint.
"""

import pytest


PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
SCREENSHOT_ID = 343286

@pytest.mark.vcr
def test_screenshots(client):
    """Tests fetching of all screenshots
    """
    screenshots = client.screenshots(PROJECT_ID)
    assert screenshots.project_id == PROJECT_ID
    assert screenshots.items[0].screenshot_id == SCREENSHOT_ID


@pytest.mark.vcr
def test_screenshots_pagination(client):
    """Tests fetching of all screenshots with pagination
    """
    screenshots = client.screenshots(PROJECT_ID, {"page": 2, "limit": 3})
    # Revise these tests after ITSD-870 is resolved:
    assert screenshots.project_id == PROJECT_ID
    assert screenshots.current_page == 2
    #assert screenshots.total_count == 26
    #assert screenshots.page_count == 7
    assert screenshots.limit == 3

    # assert not screenshots.is_last_page()
    # assert not screenshots.is_first_page()
    # assert screenshots.has_next_page()
    # assert screenshots.has_prev_page()


@pytest.mark.vcr
def test_screenshot(client):
    """Tests fetching of a screenshot
    """
    screenshot = client.screenshot(PROJECT_ID, SCREENSHOT_ID)
    assert screenshot.screenshot_id == SCREENSHOT_ID
    assert screenshot.project_id == PROJECT_ID
    assert 34089721 in screenshot.key_ids
    assert "amazonaws.com" in screenshot.url
    assert screenshot.title == "screenshot"
    assert screenshot.description == ""
    assert "test" in screenshot.screenshot_tags
    assert screenshot.width == 480
    assert screenshot.height == 800
    assert screenshot.created_at == "2019-12-27 14:52:26 (Etc/UTC)"
    assert screenshot.created_at_timestamp == 1577458346


@pytest.mark.vcr
def test_create_screenshots(client, screenshot_data):
    """Tests creation of a screenshot
    """
    screenshots = client.create_screenshots(PROJECT_ID, [{
        "data": screenshot_data,
        "title": "Python screenshot",
        "ocr": False
    }])
    assert screenshots.project_id == PROJECT_ID
    screenshot = screenshots.items[0]
    assert screenshot.title == "Python screenshot"
    assert "amazonaws.com" in screenshot.url


@pytest.mark.vcr
def test_update_screenshot(client):
    """Tests updating of a screenshot
    """
    screenshot = client.update_screenshot(PROJECT_ID, SCREENSHOT_ID, {
        "title": "Updated by Python",
        "description": "Python description"
    })
    assert screenshot.project_id == PROJECT_ID
    assert screenshot.title == "Updated by Python"
    assert screenshot.description == "Python description"


@pytest.mark.vcr
def test_delete_screenshot(client):
    """Tests deletion of a screenshot
    """
    resp = client.delete_screenshot(PROJECT_ID, 496094)
    assert resp['project_id'] == PROJECT_ID
    assert resp['screenshot_deleted']
