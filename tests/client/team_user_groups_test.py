"""
Tests for the TeamUserGroups endpoint.
"""

import pytest


TEAM_ID = 176692
GROUP_ID = 515
NEW_GROUP_ID = 2494


@pytest.mark.vcr
def test_team_user_groups(client):
    """Tests fetching of all team user groups
    """
    groups = client.team_user_groups(TEAM_ID)
    assert groups.team_id == TEAM_ID
    assert groups.items[0].group_id == GROUP_ID


@pytest.mark.vcr
def test_team_user_groups_pagination(client):
    """Tests fetching of all team user groups with pagination
    """
    groups = client.team_user_groups(TEAM_ID, {
        "page": 2,
        "limit": 1
    })
    assert groups.team_id == TEAM_ID
    assert groups.items[0].group_id == 1266
    assert groups.current_page == 2
    assert groups.total_count == 3
    assert groups.page_count == 3
    assert groups.limit == 1

    assert not groups.is_last_page()
    assert not groups.is_first_page()
    assert groups.has_next_page()
    assert groups.has_prev_page()


@pytest.mark.vcr
def test_team_user_group(client):
    """Tests fetching of a team user group
    """
    group = client.team_user_group(TEAM_ID, GROUP_ID)
    assert group.team_id == TEAM_ID
    assert group.group_id == GROUP_ID
    assert group.name == "Demo"
    assert group.permissions['is_admin']
    assert group.created_at == "2019-03-19 19:53:04 (Etc/UTC)"
    assert group.created_at_timestamp == 1553025184
    assert group.team_id == 176692
    assert "531138705d0ba0c18f5b43.63503311" in group.projects
    assert 20181 in group.members


@pytest.mark.vcr
def test_create_team_user_group(client):
    """Tests creation of a team user group
    """
    group = client.create_team_user_group(TEAM_ID, {
        "name": "Python group",
        "is_reviewer": True,
        "is_admin": True,
        "admin_rights": ["upload"]
    })
    assert group.team_id == TEAM_ID
    assert group.group_id == NEW_GROUP_ID
    assert group.name == "Python group"
    assert group.permissions['is_admin']
    assert group.permissions['is_reviewer']
    assert group.permissions['admin_rights'] == ["upload"]


@pytest.mark.vcr
def test_update_team_user_group(client):
    """Tests updating of a team user group
    """
    group = client.update_team_user_group(TEAM_ID, GROUP_ID, {
        "name": "Updated Python group",
        "is_reviewer": False,
        "is_admin": True,
        "admin_rights": ["upload"]
    })
    assert group.team_id == TEAM_ID
    assert group.group_id == GROUP_ID
    assert group.name == "Updated Python group"
    assert group.permissions['is_admin']
    assert not group.permissions['is_reviewer']


@pytest.mark.vcr
def test_delete_team_user_group(client):
    """Tests deletion of a team user group
    """
    resp = client.delete_team_user_group(TEAM_ID, NEW_GROUP_ID)
    assert resp['team_id'] == TEAM_ID
    assert resp['group_deleted']


@pytest.mark.vcr
def test_add_projects_to_group(client):
    """Tests adding projects to a team user group
    """
    group = client.add_projects_to_group(TEAM_ID, GROUP_ID,
                                         ["638597985c913f818559f3.17106287",
                                          "404021655ce68d0f36ad23.02802891"])
    assert group.team_id == TEAM_ID
    assert group.group_id == GROUP_ID
    assert "638597985c913f818559f3.17106287" in group.projects
    assert "404021655ce68d0f36ad23.02802891" in group.projects


@pytest.mark.vcr
def test_remove_projects_from_group(client):
    """Tests removing projects from a team user group
    """
    group = client.remove_projects_from_group(
        TEAM_ID,
        GROUP_ID,
        ["638597985c913f818559f3.17106287",
         "404021655ce68d0f36ad23.02802891"]
    )
    assert group.team_id == TEAM_ID
    assert group.group_id == GROUP_ID
    assert "638597985c913f818559f3.17106287" not in group.projects
    assert "404021655ce68d0f36ad23.02802891" not in group.projects


@pytest.mark.vcr
def test_add_members_to_group(client):
    """Tests adding members to a team user group
    """
    group = client.add_members_to_group(TEAM_ID, GROUP_ID, [52911, 35555])
    assert group.team_id == TEAM_ID
    assert group.group_id == GROUP_ID
    assert 52911 in group.members
    assert 35555 in group.members

@pytest.mark.vcr
def test_add_member_to_group(client):
    """Tests adding a member to a team user group
    """
    group = client.add_members_to_group(TEAM_ID, GROUP_ID, 35555)
    assert group.team_id == TEAM_ID
    assert group.group_id == GROUP_ID
    assert 35555 in group.members

@pytest.mark.vcr
def test_remove_member_from_group(client):
    """Tests removing a member from a team user group
    """
    group = client.remove_members_from_group(TEAM_ID, GROUP_ID, 35555)
    assert group.team_id == TEAM_ID
    assert group.group_id == GROUP_ID
    assert 35555 not in group.members

@pytest.mark.vcr
def test_remove_members_from_group(client):
    """Tests removing members from a team user group
    """
    group = client.remove_members_from_group(TEAM_ID, GROUP_ID, [52911, 35555])
    assert group.team_id == TEAM_ID
    assert group.group_id == GROUP_ID
    assert 52911 not in group.members
    assert 35555 not in group.members
