"""
Tests for the QueuedProcesses endpoint.
"""

import pytest


PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
SNAPSHOT_ID = 164513

@pytest.mark.vcr
def test_snapshots(client):
    """Tests fetching of all snapshots
    """
    snapshots = client.snapshots(PROJECT_ID)
    assert snapshots.project_id == PROJECT_ID
    snapshot = snapshots.items[0]
    assert snapshot.snapshot_id == SNAPSHOT_ID
    assert snapshot.title == "Pseudolocalization snapshot"
    assert snapshot.created_at == "2019-12-30 17:05:00 (Etc/UTC)"
    assert snapshot.created_at_timestamp == 1577725500
    assert snapshot.created_by == 20181
    assert snapshot.created_by_email == "bodrovis@protonmail.com"


@pytest.mark.vcr
def test_snapshots_pagination(client):
    """Tests fetching of all snapshots with pagination
    """
    snapshots = client.snapshots(PROJECT_ID, {"page": 2, "limit": 1})
    assert snapshots.project_id == PROJECT_ID
    assert snapshots.items[0].snapshot_id == 164514
    assert snapshots.current_page == 2
    assert snapshots.total_count == 2
    assert snapshots.page_count == 2
    assert snapshots.limit == 1

    assert snapshots.is_last_page()
    assert not snapshots.is_first_page()
    assert not snapshots.has_next_page()
    assert snapshots.has_prev_page()


@pytest.mark.vcr
def test_create_snapshot(client):
    """Tests creation of a snapshot
    """
    snapshot = client.create_snapshot(PROJECT_ID, {"title": "Python snapshot"})
    assert snapshot.project_id == PROJECT_ID
    assert snapshot.title == "Python snapshot"


@pytest.mark.vcr
def test_restore_snapshot(client):
    """Tests restoration of a snapshot
    """
    project = client.restore_snapshot(PROJECT_ID, SNAPSHOT_ID)
    assert project.project_id != PROJECT_ID
    assert project.name == "OnBoarding copy"


@pytest.mark.vcr
def test_delete_snapshot(client):
    """Tests deletion of a snapshot
    """
    resp = client.delete_snapshot(PROJECT_ID, SNAPSHOT_ID)
    assert resp['project_id'] == PROJECT_ID
    assert resp['snapshot_deleted']
