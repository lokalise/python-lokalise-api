"""
Tests for the Project endpoint.
"""

import pytest

PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
NEW_PROJECT_ID = "752354175ee755409bb393.87183877"


@pytest.mark.vcr
def test_all_projects(client):
    """Tests fetching of all projects
    """
    projects = client.projects()
    assert projects.project_id is None
    assert projects.is_last_page()
    assert projects.is_first_page()
    assert isinstance(projects.items[0].raw_data, dict)
    assert projects.items[0].project_id == "638597985c913f818559f3.17106287"


@pytest.mark.vcr
def test_all_projects_pagination(client):
    """Tests fetching of projects pagination
    """
    projects = client.projects({"limit": 2, "page": 3})
    assert projects.items[0].project_id == "531138705d0ba0c18f5b43.63503311"
    assert projects.current_page == 3
    assert projects.total_count == 17
    assert projects.page_count == 9
    assert projects.limit == 2

    assert not projects.is_last_page()
    assert not projects.is_first_page()
    assert projects.has_next_page()
    assert projects.has_prev_page()


@pytest.mark.vcr
def test_project(client):
    """Tests fetching of a single project
    """
    project = client.project(PROJECT_ID)

    assert project.project_id == PROJECT_ID
    assert project.project_type == "localization_files"
    assert project.name == "OnBoarding"
    assert project.description == "Demo project for onboarding course"
    assert project.created_at == "2019-12-30 12:56:07 (Etc/UTC)"
    assert project.created_at_timestamp == 1577710567
    assert project.created_by == 20181
    assert project.created_by_email == "bodrovis@protonmail.com"
    assert project.team_id == 176692
    assert project.base_language_id == 640
    assert project.base_language_iso == "en"
    assert isinstance(project.settings, dict)
    assert project.settings["per_platform_key_names"]
    assert isinstance(project.statistics, dict)
    assert project.statistics["progress_total"] == 53


@pytest.mark.vcr
def test_create_project(client):
    """Tests project creation
    """
    project = client.create_project({
        "name": "Python sample proj",
        "description": "Project created by Python client",
        "languages": [
            {
                "lang_iso": "en",
                "custom_iso": "en-us"
            },
            {
                "lang_iso": "en_GB",
                "custom_iso": "en-gb"
            }
        ],
        "base_lang_iso": "en-us"
    })

    assert project.project_id == NEW_PROJECT_ID
    assert project.name == "Python sample proj"
    assert project.description == "Project created by Python client"
    assert project.base_language_iso == "en-us"
    assert project.statistics['languages'][1]['language_iso'] == "en-gb"


@pytest.mark.vcr
def test_update_project(client):
    """Tests project update
    """
    project = client.update_project(NEW_PROJECT_ID, {
        "name": "Updated Python proj",
        "description": "Proj updated by Python"
    })

    assert project.project_id == NEW_PROJECT_ID
    assert project.name == "Updated Python proj"
    assert project.description == "Proj updated by Python"


@pytest.mark.vcr
def test_empty_project(client):
    """Tests empty project request
    """
    response = client.empty_project(NEW_PROJECT_ID)

    assert response["keys_deleted"]
    assert response["project_id"] == NEW_PROJECT_ID


@pytest.mark.vcr
def test_delete_project(client):
    """Tests project deletion
    """
    response = client.delete_project(NEW_PROJECT_ID)

    assert response["project_deleted"]
    assert response["project_id"] == NEW_PROJECT_ID


@pytest.mark.vcr
def test_project_to_string(client):
    """Tests converting the project to string
    """
    project = client.project(PROJECT_ID)
    assert PROJECT_ID in str(project)
