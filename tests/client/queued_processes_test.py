"""
Tests for the QueuedProcesses endpoint.
"""

import pytest
from lokalise.client import Client

PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
PROCESS_ID = "344f8e3fb813d10c6ec75ddcf35e2e24815af242"


@pytest.mark.vcr
def test_queued_processes(client: Client) -> None:
    """Tests fetching of all queued processes"""
    processes = client.queued_processes(f"{PROJECT_ID}:python-branch-upd")
    assert processes.project_id == PROJECT_ID
    assert processes.branch == "python-branch-upd"
    assert processes.items[0].process_id == PROCESS_ID


@pytest.mark.vcr
def test_queued_process(client: Client) -> None:
    """Tests fetching of a queued process"""
    process = client.queued_process(f"{PROJECT_ID}:python-branch-upd", PROCESS_ID)
    assert process.project_id == PROJECT_ID
    assert process.branch == "python-branch-upd"
    assert process.process_id == PROCESS_ID
    assert process.type == "file-import"
    assert process.status == "finished"
    assert process.message == ""
    assert process.created_by == 20181
    assert process.created_by_email == "bodrovis@protonmail.com"
    assert process.created_at == "2020-06-19 11:42:02 (Etc/UTC)"
    assert process.created_at_timestamp == 1592566922
    assert process.details["files"][0]["status"] == "finished"
    assert process.details["files"][0]["name_original"] == "en.json"


@pytest.mark.vcr
def test_queued_process_async_download(client: Client) -> None:
    """Tests fetching of a queued process for an async download"""
    project_id = "6504960967ab53d45e0ed7.15877499"
    process_id = "1efed4e6-461a-6d6e-a779-dea3ae8b7e9e"
    process = client.queued_process(project_id, process_id)

    assert process.process_id == process_id
    assert process.type == "async-export"
    assert process.status == "finished"
    assert "https://lokalise-live-lok-s3-fss-export" in process.details["download_url"]
