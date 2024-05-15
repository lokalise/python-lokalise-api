"""
Tests for the Keys endpoint.
"""

import pytest

PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
PROJECT_ID2 = "2273827860c1e2473eb195.11207948"
KEY_ID = 34089721


@pytest.mark.vcr
def test_keys(client):
    """Tests fetching of all keys
    """
    keys = client.keys(PROJECT_ID, {
        "page": 2,
        "limit": 3,
        "disable_references": "1",
        "filter_archived": "exclude"
    })
    assert keys.project_id == PROJECT_ID
    assert keys.items[0].key_id == KEY_ID
    assert keys.current_page == 2
    assert keys.total_count == 13
    assert keys.page_count == 5
    assert keys.limit == 3

    assert not keys.is_last_page()
    assert not keys.is_first_page()
    assert keys.has_next_page()
    assert keys.has_prev_page()
    assert not keys.has_next_cursor()
    assert keys.next_cursor is None

@pytest.mark.vcr
def test_keys_cursor(client):
    """Tests fetching of keys with cursor
    """
    keys = client.keys(PROJECT_ID2, {
        "disable_references": "1",
        "limit": 2,
        "pagination": "cursor",
        "cursor": "eyIxIjo0NDU5NjA2MX0="
    })
    assert keys.project_id == PROJECT_ID2
    assert keys.items[0].key_id == 94981678
    assert keys.current_page == 0
    assert keys.total_count == 0
    assert keys.page_count == 0
    assert keys.limit == 2
    assert keys.next_cursor == "eyIxIjoyNTU5ODU3MTB9"

    assert keys.has_next_cursor()
    assert not keys.has_next_page()
    assert not keys.has_prev_page()

@pytest.mark.vcr
def test_create_keys(client):
    """Tests creation of translation keys
    """
    keys = client.create_keys(PROJECT_ID, [
        {
            "key_name": "python_1",
            "platforms": ["ios", "android"],
            "description": "Created by Python"
        },
        {
            "key_name": "python_2",
            "platforms": ["web"],
            "translations": [
                {
                    "language_iso": "en",
                    "translation": "Hi from Python"
                }
            ]
        }
    ])
    assert keys.project_id == PROJECT_ID
    assert len(keys.items) == 2
    key_1 = keys.items[0]
    key_2 = keys.items[1]
    assert key_1.key_name['ios'] == "python_1"
    assert "ios" in key_1.platforms
    assert "web" not in key_1.platforms
    assert key_1.description == "Created by Python"
    assert key_2.key_name['web'] == "python_2"
    assert "ios" not in key_2.platforms
    assert "web" in key_2.platforms
    assert key_2.translations[2]["language_iso"] == "en"
    assert key_2.translations[2]["translation"] == "Hi from Python"


@pytest.mark.vcr
def test_create_key(client):
    """Tests creation of a single key
    """
    keys = client.create_keys(PROJECT_ID, {
        "key_name": "python_3",
        "platforms": ["ios", "android"],
        "translations": [
            {
                "language_iso": "ru_RU",
                "translation": "Привет от Python"
            }
        ]
    })
    assert keys.project_id == PROJECT_ID
    key = keys.items[0]
    assert key.key_name['ios'] == "python_3"
    assert "ios" in key.platforms
    assert "web" not in key.platforms
    assert key.translations[0]["language_iso"] == "ru_RU"
    assert key.translations[0]["translation"] == "Привет от Python"


@pytest.mark.vcr
def test_key(client):
    """Tests fetching of a key
    """
    key = client.key(PROJECT_ID, KEY_ID, {"disable_references": "1"})
    assert key.project_id == PROJECT_ID
    assert key.branch == 'master'
    assert key.key_id == KEY_ID
    assert key.created_at == "2019-12-27 12:53:16 (Etc/UTC)"
    assert key.created_at_timestamp == 1577451196
    assert key.key_name['ios'] == "manual_setup"
    assert key.filenames['android'] == ''
    assert key.description == 'Updated by Python'
    assert "web" in key.platforms
    assert "python" in key.tags
    assert key.comments == []
    assert key.screenshots[0]['screenshot_id'] == 343286
    assert key.translations[0]['translation_id'] == 220681440
    assert not key.is_plural
    assert key.plural_name == ''
    assert not key.is_hidden
    assert not key.is_archived
    assert key.context == ''
    assert key.base_words == 2
    assert key.char_limit == 0
    assert key.custom_attributes == ''
    assert key.modified_at == "2020-06-20 13:02:37 (Etc/UTC)"
    assert key.modified_at_timestamp == 1592658157
    assert key.translations_modified_at == "2020-06-20 12:42:24 (Etc/UTC)"
    assert key.translations_modified_at_timestamp == 1592656944


@pytest.mark.vcr
def test_update_key(client):
    """Tests updating of a key
    """
    key = client.update_key(PROJECT_ID, KEY_ID, {
        "description": "Updated by Python",
        "tags": ["python"]
    })
    assert key.project_id == PROJECT_ID
    assert key.key_id == KEY_ID
    assert key.description == "Updated by Python"
    assert "python" in key.tags
    assert key.modified_at_timestamp == 1592658157


@pytest.mark.vcr
def test_update_keys(client):
    """Tests bulk key update
    """
    keys = client.update_keys(PROJECT_ID, [
        {
            "key_id": 48855757,
            "description": "Bulk updated",
            "tags": ["bulk-python"]
        },
        {
            "key_id": 48855758,
            "translations": [
                {
                    "language_iso": "ru_RU",
                    "translation": "Обновлённый перевод Python"
                }
            ]
        }
    ])
    assert keys.project_id == PROJECT_ID
    assert len(keys.items) == 2
    key_1 = keys.items[0]
    key_2 = keys.items[1]
    assert key_1.key_id == 48855757
    assert key_1.description == "Bulk updated"
    assert "bulk-python" in key_1.tags
    assert key_2.key_id == 48855758
    assert key_2.translations[0]["language_iso"] == "ru_RU"
    assert key_2.translations[0]["translation"] == "Обновлённый перевод Python"


@pytest.mark.vcr
def test_delete_key(client):
    """Tests a single key deletion
    """
    resp = client.delete_key(PROJECT_ID, 48855760)
    assert resp['project_id'] == PROJECT_ID
    assert resp['key_removed']


@pytest.mark.vcr
def test_delete_keys(client):
    """Tests deletion of multiple keys in bulk
    """
    resp = client.delete_keys(PROJECT_ID, [48855757, 48855758])
    assert resp['project_id'] == PROJECT_ID
    assert resp['keys_removed']
