"""
Tests for the QueuedProcesses endpoint.
"""

import pytest

PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
PROCESS_ID = "344f8e3fb813d10c6ec75ddcf35e2e24815af242"


@pytest.mark.vcr
def test_queued_processes(client):
    """Tests fetching of all queued processes
    """
    processes = client.queued_processes(f"{PROJECT_ID}:python-branch-upd")
    assert processes.project_id == PROJECT_ID
    assert processes.branch == 'python-branch-upd'
    assert processes.items[0].process_id == PROCESS_ID


@pytest.mark.vcr
def test_queued_process(client):
    """Tests fetching of a queued process
    """
    process = client.queued_process(
        f"{PROJECT_ID}:python-branch-upd",
        PROCESS_ID
    )
    assert process.project_id == PROJECT_ID
    assert process.branch == 'python-branch-upd'
    assert process.process_id == PROCESS_ID
    assert process.type == 'file-import'
    assert process.status == 'finished'
    assert process.message == ''
    assert process.created_by == 20181
    assert process.created_by_email == "bodrovis@protonmail.com"
    assert process.created_at == "2020-06-19 11:42:02 (Etc/UTC)"
    assert process.created_at_timestamp == 1592566922
    assert process.details['files'][0]['status'] == 'finished'
    assert process.details['files'][0]['name_original'] == 'en.json'
