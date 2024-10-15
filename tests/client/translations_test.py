"""
Tests for the Translations endpoint.
"""

import pytest


PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
ANOTHER_PROJECT_ID = "803826145ba90b42d5d860.46800099"
ANOTHER_TRANSLATION_ID = 304581218
TRANSLATION_ID = 220681425


@pytest.mark.vcr
def test_translations(client):
    """Tests fetching of all translations
    """
    translations = client.translations(PROJECT_ID)
    assert translations.project_id == PROJECT_ID
    assert translations.items[0].translation_id == TRANSLATION_ID


@pytest.mark.vcr
def test_translations_pagination(client):
    """Tests fetching of all translations with pagination
    """
    translations = client.translations(PROJECT_ID, {
        "page": 2,
        "limit": 5,
        "disable_references": "1",
        "filter_untranslated": 1
    })
    assert translations.project_id == PROJECT_ID
    assert translations.items[0].translation_id == 220681461
    assert translations.current_page == 2
    assert translations.total_count == 21
    assert translations.page_count == 5
    assert translations.limit == 5
    assert translations.next_cursor is None

    assert not translations.is_last_page()
    assert not translations.has_next_cursor()
    assert not translations.is_first_page()
    assert translations.has_next_page()
    assert translations.has_prev_page()


@pytest.mark.vcr
def test_translations_pagination_cursor(client):
    """Tests fetching of all translations with pagination and cursor
    """
    translations = client.translations(ANOTHER_PROJECT_ID, {
        "limit": 2,
        "disable_references": "1",
        "filter_untranslated": 1,
        "pagination": "cursor",
        "cursor": "eyIxIjozMDQ1ODEyMTJ9"
    })
    assert translations.project_id == ANOTHER_PROJECT_ID
    assert translations.items[0].translation_id == 304581213
    assert translations.current_page == 0
    assert translations.total_count == 0
    assert translations.page_count == 0
    assert translations.limit == 2
    assert translations.next_cursor == "eyIxIjozMDQ1ODEyMjN9"

    assert translations.has_next_cursor()


@pytest.mark.vcr
def test_translation(client):
    """Tests fetching of a translation
    """
    translation = client.translation(
        ANOTHER_PROJECT_ID, ANOTHER_TRANSLATION_ID, {
            "disable_references": 1})
    assert translation.project_id == ANOTHER_PROJECT_ID
    assert translation.translation_id == ANOTHER_TRANSLATION_ID
    assert translation.key_id == 44596059
    assert translation.language_iso == "ru"
    assert translation.modified_at == "2020-05-15 10:44:42 (Etc/UTC)"
    assert translation.modified_at_timestamp == 1589539482
    assert translation.modified_by == 20181
    assert translation.modified_by_email == "bodrovis@protonmail.com"
    assert translation.translation == "Сообщение"
    assert not translation.is_fuzzy
    assert not translation.is_reviewed
    assert translation.reviewed_by == 0
    assert translation.words == 1
    assert translation.custom_translation_statuses == []


@pytest.mark.vcr
def test_update_translation(client):
    """Tests updating of a translation
    """
    translation = client.update_translation(PROJECT_ID, TRANSLATION_ID, {
        "translation": "Приветствуем в Sample App, [%s:name]!",
        "custom_translation_status_ids": [429]
    })
    assert translation.project_id == PROJECT_ID
    assert translation.translation_id == TRANSLATION_ID
    assert translation.translation == "Приветствуем в Sample App, [%s:name]!"
    assert translation.custom_translation_statuses[0]['status_id'] == 429
