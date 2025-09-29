"""
Tests for the Languages and SystemLanguages endpoint.
"""

import pytest
from lokalise.client import Client

PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
LANG_ID = 10153


@pytest.mark.vcr
def test_system_languages(client: Client) -> None:
    """Tests fetching of all system languages"""
    s_langs = client.system_languages({"page": 2, "limit": 10})
    assert s_langs.current_page == 2
    assert s_langs.total_count == 654
    assert s_langs.page_count == 66
    assert s_langs.limit == 10

    assert not s_langs.is_last_page()
    assert not s_langs.is_first_page()
    assert s_langs.has_next_page()
    assert s_langs.has_prev_page()
    lang = s_langs.items[0]
    assert lang.lang_id == 714
    assert lang.lang_iso == "ar"


@pytest.mark.vcr
def test_project_languages(client: Client) -> None:
    """Tests fetching of project languages"""
    langs = client.project_languages(PROJECT_ID, {"page": 2, "limit": 3})
    assert langs.current_page == 2
    assert langs.total_count == 6
    assert langs.page_count == 2
    assert langs.limit == 3

    assert langs.is_last_page()
    assert not langs.is_first_page()
    assert not langs.has_next_page()
    assert langs.has_prev_page()

    assert langs.project_id == PROJECT_ID
    assert langs.branch == "master"
    assert len(langs.items) == 3

    assert langs.items[0].lang_iso == "de_DE"


@pytest.mark.vcr
def test_create_languages(client: Client) -> None:
    """Tests creation of project languages"""
    langs = client.create_languages(
        PROJECT_ID,
        [
            {"lang_iso": "ar", "custom_name": "Custom AR"},
            {"lang_iso": "be_BY", "custom_iso": "by_2"},
        ],
    )

    assert langs.project_id == PROJECT_ID
    items = langs.items
    assert items[0].lang_iso == "ar"
    assert items[0].lang_name == "Custom AR"
    assert items[1].lang_iso == "by_2"
    assert items[1].lang_name == "Belarusian (Belarus)"


@pytest.mark.vcr
def test_create_language(client: Client) -> None:
    """Tests creation of a single project language"""
    langs = client.create_languages(PROJECT_ID, {"lang_iso": "fr"})

    item = langs.items[0]
    assert item.lang_iso == "fr"
    assert item.lang_name == "French"


@pytest.mark.vcr
def test_language(client: Client) -> None:
    """Tests fetching of a project language"""
    lang = client.language(PROJECT_ID, LANG_ID)
    assert lang.branch == "master"
    assert lang.project_id == PROJECT_ID
    assert lang.lang_id == LANG_ID
    assert lang.lang_iso == "lv"
    assert lang.lang_name == "Latvian"
    assert not lang.is_rtl
    assert lang.plural_forms[0] == "zero"


@pytest.mark.vcr
def test_update_language(client: Client) -> None:
    """Tests updating of a project language"""
    lang = client.update_language(PROJECT_ID, LANG_ID, {"lang_name": "Custom LV"})
    assert lang.branch == "master"
    assert lang.project_id == PROJECT_ID
    assert lang.lang_id == LANG_ID
    assert lang.lang_iso == "lv"
    assert lang.lang_name == "Custom LV"


@pytest.mark.vcr
def test_delete_language(client: Client) -> None:
    """Tests deletion of a project language"""
    response = client.delete_language(PROJECT_ID, LANG_ID)
    assert response["project_id"] == PROJECT_ID
    assert response["language_deleted"]
