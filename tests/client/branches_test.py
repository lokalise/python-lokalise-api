"""
Tests for the Branches endpoint.
"""

import pytest


PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
BRANCH_ID = 55312

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
    # assert branches.current_page == 2
    # assert branches.total_count == 6
    # assert branches.page_count == 2
    # assert branches.limit == 3
    #
    # assert branches.is_last_page()
    # assert not branches.is_first_page()
    # assert not branches.has_next_page()
    # assert branches.has_prev_page()
