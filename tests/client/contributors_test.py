import pytest

PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
CONTRIBUTOR_ID = 20181


@pytest.mark.vcr
def test_all_contributors(client):
    contributors = client.contributors(PROJECT_ID)
    assert contributors.project_id == PROJECT_ID
    assert contributors.items[0].user_id == 20181


@pytest.mark.vcr
def test_all_contributors_pagination(client):
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
def test_contributor(client):
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


@pytest.mark.vcr
def test_contributor_to_string(client):
    contributor = client.contributor(PROJECT_ID, CONTRIBUTOR_ID)
    assert str(CONTRIBUTOR_ID) in str(contributor)
