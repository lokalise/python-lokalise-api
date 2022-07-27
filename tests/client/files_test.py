"""
Tests for the Files endpoint.
"""

import pytest

PROJECT_ID = "454087345e09f3e7e7eae3.57891254"


@pytest.mark.vcr
def test_files(client):
    """Tests fetching of all files
    """
    files = client.files(PROJECT_ID)
    assert files.project_id == PROJECT_ID
    assert files.items[0].filename == "%LANG_ISO%.xml"


@pytest.mark.vcr
def test_files_pagination(client):
    """Tests fetching of all files with pagination
    """
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
def test_upload_file(client):
    """Tests file uploading in background
    """
    process = client.upload_file(PROJECT_ID, {
        "data": 'ZnI6DQogIHRlc3Q6IHRyYW5zbGF0aW9u',
        "filename": 'python_upload.yml',
        "lang_iso": 'ru_RU'
    })
    assert process.project_id == PROJECT_ID
    assert process.process_id == "9db05dcdce6a15e2550051d13d5eb39c700bf8dd"
    assert process.type == "file-import"
    assert process.status == "queued"


@pytest.mark.vcr
def test_download_files(client):
    """Tests files downloading
    """
    response = client.download_files(PROJECT_ID, {
        "format": "json",
        "original_filenames": True,
        "replace_breaks": False
    })
    assert response['project_id'] == PROJECT_ID
    assert r"amazonaws.com" in response['bundle_url']


@pytest.mark.vcr
def test_delete_file(client):
    """Tests file deletion
    """
    docs_file_project_id = "507504186242fccb32f015.15252556"

    response = client.delete_file(docs_file_project_id, 1161474)
    assert response['project_id'] == docs_file_project_id
    assert response['file_deleted']
