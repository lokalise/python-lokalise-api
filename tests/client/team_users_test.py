"""
Tests for the TeamUsers endpoint.
"""

import pytest


TEAM_ID = 176692
USER_ID = 52911


@pytest.mark.vcr
def test_team_users(client):
    """Tests fetching of all team users
    """
    users = client.team_users(TEAM_ID)
    assert users.team_id == TEAM_ID
    assert users.items[0].user_id == 68139


@pytest.mark.vcr
def test_team_users_pagination(client):
    """Tests fetching of all team users with pagination
    """
    users = client.team_users(TEAM_ID, {
        "page": 2,
        "limit": 4
    })
    assert users.team_id == TEAM_ID
    assert users.items[0].user_id == USER_ID
    assert users.current_page == 2
    assert users.total_count == 16
    assert users.page_count == 4
    assert users.limit == 4

    assert not users.is_last_page()
    assert not users.is_first_page()
    assert users.has_next_page()
    assert users.has_prev_page()


@pytest.mark.vcr
def test_team_user(client):
    """Tests fetching of a team user
    """
    user = client.team_user(TEAM_ID, USER_ID)
    assert user.team_id == TEAM_ID
    assert user.user_id == USER_ID
    assert user.email == "elf@lorien.com"
    assert user.fullname == "Mr. Elf"
    assert user.created_at == "2019-12-29 13:47:23 (Etc/UTC)"
    assert user.created_at_timestamp == 1577627243
    assert user.role == "member"


@pytest.mark.vcr
def test_update_team_user(client):
    """Tests updating of a team user
    """
    user = client.update_team_user(TEAM_ID, USER_ID, {"role": "admin"})
    assert user.team_id == TEAM_ID
    assert user.user_id == USER_ID
    assert user.role == "admin"


@pytest.mark.vcr
def test_delete_team_user(client):
    """Tests deletion of a team user
    """
    resp = client.delete_team_user(TEAM_ID, 68139)
    assert resp['team_id'] == TEAM_ID
    assert resp['team_user_deleted']
