"""
Tests for the Branches endpoint.
"""

import pytest


PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
BRANCH_ID = 55312
NEW_BRANCH_ID = 66307


@pytest.mark.vcr
def test_all_branches(client):
    """Tests fetching of all branches
    """
    branches = client.branches(PROJECT_ID)
    assert branches.project_id == PROJECT_ID
    assert branches.items[0].branch_id == BRANCH_ID


@pytest.mark.vcr
def test_all_branches_pagination(client):
    """Tests fetching of all branches with pagination params
    """
    branches = client.branches(PROJECT_ID, {"page": 2, "limit": 1})
    assert branches.project_id == PROJECT_ID
    assert branches.items[0].branch_id == 45845
    # revise these tests once ITSD-854 is resolved
    assert branches.current_page == 2
    assert branches.total_count == 1
    assert branches.page_count == 1
    assert branches.limit == 1

    # assert branches.is_last_page()
    # assert branches.is_first_page()
    # assert not branches.has_next_page()
    # assert not branches.has_prev_page()


@pytest.mark.vcr
def test_branch(client):
    """Tests fetching of a single branch
    """
    branch = client.branch(PROJECT_ID, BRANCH_ID)
    assert branch.project_id == PROJECT_ID
    assert branch.branch_id == BRANCH_ID
    assert branch.name == "deutch"
    assert branch.created_at == "2020-04-03 14:41:46 (Etc/UTC)"
    assert branch.created_at_timestamp == 1585924906
    assert branch.created_by == 20181
    assert branch.created_by_email == "bodrovis@protonmail.com"


@pytest.mark.vcr
def test_create_branch(client):
    """Tests creation of a branch
    """
    branch = client.create_branch(PROJECT_ID, {"name": "python-branch"})
    assert branch.project_id == PROJECT_ID
    assert branch.branch_id == NEW_BRANCH_ID
    assert branch.name == "python-branch"


@pytest.mark.vcr
def test_update_branch(client):
    """Tests updating of a branch
    """
    branch = client.update_branch(PROJECT_ID, NEW_BRANCH_ID,
                                  {"name": "python-branch-updated"})
    assert branch.project_id == PROJECT_ID
    assert branch.branch_id == NEW_BRANCH_ID
    assert branch.name == "python-branch-updated"


@pytest.mark.vcr
def test_delete_branch(client):
    """Tests deletion of a branch
    """
    response = client.delete_branch(PROJECT_ID, NEW_BRANCH_ID)
    assert response['project_id'] == PROJECT_ID
    assert response['branch_deleted']


@pytest.mark.vcr
def test_merge_branch(client):
    """Tests branch merging
    """
    response = client.merge_branch(PROJECT_ID, BRANCH_ID,
                                   {"force_conflict_resolve_using": "target"})
    assert response['project_id'] == PROJECT_ID
    assert response['branch_merged']
    assert response['branch']['branch_id'] == BRANCH_ID
