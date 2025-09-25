"""
Tests for the Files endpoint.
"""

import pytest
from lokalise.client import Client

PROJECT_ID = "454087345e09f3e7e7eae3.57891254"


@pytest.mark.vcr
def test_files(client: Client) -> None:
    """Tests fetching of all files"""
    project_id = "71749499610303a83ad8a2.67103833"
    files = client.files(project_id)
    assert files.project_id == project_id
    assert files.items[0].filename == "%LANG_ISO%.yml"
    assert files.items[0].file_id == 839819


@pytest.mark.vcr
def test_files_pagination(client: Client) -> None:
    """Tests fetching of all files with pagination"""
    files = client.files(PROJECT_ID, {"page": 2, "limit": 1})
    assert files.project_id == PROJECT_ID
    file = files.items[0]
    assert file.filename == "%LANG_ISO%.yml"
    assert file.key_count == 4

    assert files.current_page == 2
    assert files.total_count == 3
    assert files.page_count == 3
    assert files.limit == 1

    assert not files.is_last_page()
    assert not files.is_first_page()
    assert files.has_next_page()
    assert files.has_prev_page()


@pytest.mark.vcr
def test_upload_file(client: Client) -> None:
    """Tests file uploading in background"""
    process = client.upload_file(
        PROJECT_ID,
        {
            "data": "ZnI6DQogIHRlc3Q6IHRyYW5zbGF0aW9u",
            "filename": "python_upload.yml",
            "lang_iso": "ru_RU",
        },
    )
    assert process.project_id == PROJECT_ID
    assert process.process_id == "9db05dcdce6a15e2550051d13d5eb39c700bf8dd"
    assert process.type == "file-import"
    assert process.status == "queued"


@pytest.mark.vcr
def test_download_files(client: Client) -> None:
    """Tests files downloading"""
    response = client.download_files(
        PROJECT_ID, {"format": "json", "original_filenames": True, "replace_breaks": False}
    )
    assert response["project_id"] == PROJECT_ID
    assert r"amazonaws.com" in response["bundle_url"]
    assert "_response_too_big" not in response


@pytest.mark.vcr
def test_download_files_too_big(client: Client) -> None:
    """Tests files downloading with X-Response-Too-Big header"""
    with pytest.warns(UserWarning, match="Project is too big for sync export"):
        response = client.download_files(
            PROJECT_ID, {"format": "json", "original_filenames": True, "replace_breaks": False}
        )

    assert response["project_id"] == PROJECT_ID
    assert r"amazonaws.com" in response["bundle_url"]
    assert "_response_too_big" in response


@pytest.mark.vcr
def test_download_files_async(client: Client) -> None:
    """Tests async files downloading"""
    process = client.download_files_async(
        "6504960967ab53d45e0ed7.15877499",
        {"format": "json", "original_filenames": True, "replace_breaks": False},
    )

    assert process.process_id == "1efed4e6-461a-6d6e-a779-dea3ae8b7e9e"


@pytest.mark.vcr
def test_delete_file(client: Client) -> None:
    """Tests file deletion"""
    docs_file_project_id = "507504186242fccb32f015.15252556"

    response = client.delete_file(docs_file_project_id, 1161474)
    assert response["project_id"] == docs_file_project_id
    assert response["file_deleted"]
