"""
Tests for the Contributors endpoint.
"""

import pytest
from lokalise.client import Client

PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
CONTRIBUTOR_ID = 20181
NEW_CONTRIBUTOR_ID = 68139


@pytest.mark.vcr
def test_all_contributors(client: Client) -> None:
    """Tests fetching of all contributors"""
    contributors = client.contributors(PROJECT_ID)
    assert contributors.project_id == PROJECT_ID
    assert contributors.items[0].user_id == 20181


@pytest.mark.vcr
def test_all_contributors_pagination(client: Client) -> None:
    """Tests fetching of all contributors with pagination"""
    contributors = client.contributors(PROJECT_ID, {"limit": 3, "page": 2})
    assert contributors.items[0].user_id == 34051
    assert contributors.current_page == 2
    assert contributors.total_count == 6
    assert contributors.page_count == 2
    assert contributors.limit == 3

    assert contributors.is_last_page()
    assert not contributors.is_first_page()
    assert not contributors.has_next_page()
    assert contributors.has_prev_page()


@pytest.mark.vcr
def test_contributor(client: Client) -> None:
    """Tests fetching of a single contributor"""
    contributor = client.contributor(PROJECT_ID, CONTRIBUTOR_ID)

    assert contributor.project_id == PROJECT_ID
    assert contributor.user_id == CONTRIBUTOR_ID
    assert contributor.email == "bodrovis@protonmail.com"
    assert contributor.fullname == "Ilya B"
    assert contributor.created_at == "2018-08-21 15:35:25 (Etc/UTC)"
    assert contributor.created_at_timestamp == 1534865725
    assert contributor.is_admin
    assert contributor.is_reviewer
    assert contributor.languages[0]["lang_id"] == 10052
    assert contributor.admin_rights[0] == "upload"
    assert contributor.role_id == 5


@pytest.mark.vcr
def test_current_contributor(client: Client) -> None:
    """Tests fetching of current contributor"""
    contributor = client.current_contributor("5868381966b39e5053ff15.63486389")

    assert contributor.user_id == CONTRIBUTOR_ID
    assert contributor.fullname == "Ilya B"


@pytest.mark.vcr
def test_create_contributors(client: Client) -> None:
    """Tests creation of multiple contributors"""
    contributors = client.create_contributors(
        PROJECT_ID,
        [
            {
                "email": "demo@python.org",
                "fullname": "Python demo 1",
                "languages": [{"lang_iso": "en", "is_writable": False}],
            },
            {
                "email": "demo2@python.org",
                "fullname": "Python demo 2",
                "languages": [{"lang_iso": "en", "is_writable": True}],
            },
        ],
    )

    assert contributors.project_id == PROJECT_ID
    assert contributors.branch == "master"
    items = contributors.items
    assert items[0].email == "demo@python.org"
    assert items[0].fullname == "Python demo 1"
    assert items[0].languages[0]["lang_iso"] == "en"
    assert not items[0].languages[0]["is_writable"]
    assert items[1].email == "demo2@python.org"
    assert items[1].fullname == "Python demo 2"
    assert items[1].languages[0]["lang_iso"] == "en"
    assert items[1].languages[0]["is_writable"]


@pytest.mark.vcr
def test_create_contributor(client: Client) -> None:
    """Tests creation of a single contributor"""
    contributors = client.create_contributors(
        PROJECT_ID,
        {
            "email": "demo3@python.org",
            "fullname": "Python demo 3",
            "languages": [{"lang_iso": "ru_RU", "is_writable": True}],
        },
    )

    assert contributors.project_id == PROJECT_ID
    assert contributors.branch == "master"
    items = contributors.items
    assert items[0].email == "demo3@python.org"
    assert items[0].fullname == "Python demo 3"
    assert items[0].languages[0]["lang_iso"] == "ru_RU"
    assert items[0].languages[0]["is_writable"]


@pytest.mark.vcr
def test_update_contributor(client: Client) -> None:
    """Tests contributor updating"""
    contributor = client.update_contributor(
        PROJECT_ID,
        NEW_CONTRIBUTOR_ID,
        {
            "is_reviewer": True,
            "languages": [
                {"lang_iso": "ru_RU", "is_writable": True},
                {"lang_iso": "en", "is_writable": False},
            ],
        },
    )
    assert contributor.user_id == NEW_CONTRIBUTOR_ID
    assert contributor.email == "demo3@python.org"
    assert not contributor.is_admin
    assert contributor.is_reviewer
    assert contributor.languages[0]["lang_iso"] == "en"
    assert not contributor.languages[0]["is_writable"]
    assert contributor.languages[1]["lang_iso"] == "ru_RU"
    assert contributor.languages[1]["is_writable"]


@pytest.mark.vcr
def test_delete_contributor(client: Client) -> None:
    """Tests contributor deletion"""
    response = client.delete_contributor(PROJECT_ID, NEW_CONTRIBUTOR_ID)
    assert response["project_id"] == PROJECT_ID
    assert response["contributor_deleted"]


@pytest.mark.vcr
def test_contributor_to_string(client: Client) -> None:
    """Tests converting contributor to string"""
    contributor = client.contributor(PROJECT_ID, CONTRIBUTOR_ID)
    assert str(CONTRIBUTOR_ID) in str(contributor)
