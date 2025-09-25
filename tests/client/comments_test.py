"""
Tests for the Comments endpoint.
"""

import pytest
from lokalise.client import Client

PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
KEY_ID = 34089718
COMMENT_ID = 3838530


@pytest.mark.vcr
def test_project_comments(client: Client) -> None:
    """Tests fetching of all project comments"""
    comments = client.project_comments(PROJECT_ID)
    assert comments.project_id == PROJECT_ID
    assert comments.items[0].comment_id == COMMENT_ID


@pytest.mark.vcr
def test_project_comments_pagination(client: Client) -> None:
    """Tests fetching of all project comments with pagination"""
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


@pytest.mark.vcr
def test_key_comments(client: Client) -> None:
    """Tests fetching of all key comments"""
    comments = client.key_comments(PROJECT_ID, KEY_ID)
    assert comments.project_id == PROJECT_ID
    assert comments.items[0].comment == "welcome key"


@pytest.mark.vcr
def test_key_comments_pagination(client: Client) -> None:
    """Tests fetching of all key comments with pagination"""
    comments = client.key_comments(PROJECT_ID, KEY_ID, {"limit": 1, "page": 2})
    assert comments.project_id == PROJECT_ID
    assert comments.items[0].comment_id == 6892379
    assert comments.current_page == 2
    assert comments.total_count == 3
    assert comments.page_count == 3
    assert comments.limit == 1

    assert not comments.is_last_page()
    assert not comments.is_first_page()
    assert comments.has_next_page()
    assert comments.has_prev_page()


@pytest.mark.vcr
def test_key_comment(client: Client) -> None:
    """Tests fetching of a key comment"""
    comment = client.key_comment(PROJECT_ID, KEY_ID, COMMENT_ID)
    assert comment.project_id == PROJECT_ID
    assert comment.comment_id == COMMENT_ID
    assert comment.key_id == KEY_ID
    assert comment.comment == "welcome key"
    assert comment.added_by == 20181
    assert comment.added_by_email == "bodrovis@protonmail.com"
    assert comment.added_at == "2019-12-26 15:09:46 (Etc/UTC)"
    assert comment.added_at_timestamp == 1577372986


@pytest.mark.vcr
def test_create_key_comments(client: Client) -> None:
    """Tests multiple key comments creation"""
    comments = client.create_key_comments(
        PROJECT_ID, KEY_ID, [{"comment": "python 1"}, {"comment": "python 2"}]
    )
    assert comments.project_id == PROJECT_ID
    items = comments.items
    assert len(items) == 2
    assert items[0].comment == "python 1"
    assert items[1].comment == "python 2"


@pytest.mark.vcr
def test_create_key_comment(client: Client) -> None:
    """Tests a single key comment creation"""
    comments = client.create_key_comments(PROJECT_ID, KEY_ID, {"comment": "python single"})
    assert comments.project_id == PROJECT_ID
    items = comments.items
    assert len(items) == 1
    assert items[0].comment == "python single"


@pytest.mark.vcr
def test_delete_key_comment(client: Client) -> None:
    """Tests key comment deletion"""
    response = client.delete_key_comment(PROJECT_ID, KEY_ID, 3838530)
    assert response["project_id"] == PROJECT_ID
    assert response["comment_deleted"]
