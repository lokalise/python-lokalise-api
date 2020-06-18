"""
Tests for the Comments endpoint.
"""

import pytest

PROJECT_ID = "454087345e09f3e7e7eae3.57891254"

@pytest.mark.vcr
def test_project_comments(client):
    """Tests fetching of all project comments
    """
    comments = client.project_comments(PROJECT_ID)
    assert comments.project_id == PROJECT_ID
    assert comments.items[0].comment_id == 3838530


@pytest.mark.vcr
def test_project_comments_pagination(client):
    """Tests fetching of all project comments with pagination
    """
    comments = client.project_comments(PROJECT_ID, {"page": 2, "limit": 1})
    assert comments.project_id == PROJECT_ID
    assert comments.items[0].comment_id == 6892379
    assert comments.current_page == 2
    assert comments.total_count == 2
    assert comments.page_count == 2
    assert comments.limit == 1

    assert comments.is_last_page()
    assert not comments.is_first_page()
    assert not comments.has_next_page()
    assert comments.has_prev_page()
