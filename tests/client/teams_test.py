"""
Tests for the Teams endpoint.
"""

import pytest
from lokalise.client import Client

TEAM_ID = 176692


@pytest.mark.vcr
def test_teams(client: Client) -> None:
    """Tests fetching of all teams"""
    teams = client.teams()
    team = teams.items[0]
    assert team.team_id == 199048
    assert team.name == "Sample"
    assert team.created_at == "2019-12-25 13:50:00 (Etc/UTC)"
    assert team.created_at_timestamp == 1577281800
    assert team.plan == "Trial"
    assert team.quota_usage["users"] == 1
    assert team.quota_allowed["users"] == 999999999


@pytest.mark.vcr
def test_teams_pagination(client: Client) -> None:
    """Tests fetching of all teams with pagination"""
    teams = client.teams({"page": 2, "limit": 3})
    assert teams.items[0].team_id == 170312
    assert teams.current_page == 2
    assert teams.total_count == 4
    assert teams.page_count == 2
    assert teams.limit == 3

    assert teams.is_last_page()
    assert not teams.is_first_page()
    assert not teams.has_next_page()
    assert teams.has_prev_page()


@pytest.mark.vcr
def test_team(client: Client) -> None:
    """Tests fetching of a team"""
    team = client.team(TEAM_ID)

    assert team.team_id == TEAM_ID
    assert team.name == "Ilya's Team"
