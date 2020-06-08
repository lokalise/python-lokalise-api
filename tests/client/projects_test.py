import pytest

project_id = "454087345e09f3e7e7eae3.57891254"

@pytest.mark.vcr
def test_all_projects(client):
    projects = client.projects()
    assert projects.is_last_page()
    assert projects.is_first_page()
    assert isinstance(projects.items[0].raw_data, dict)
    assert projects.items[0].project_id == "638597985c913f818559f3.17106287"

@pytest.mark.vcr
def test_all_projects_pagination(client):
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
    project = client.project(project_id)

    assert project.project_id == project_id
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
def test_project_to_string(client):
    project = client.project(project_id)
    assert project_id in str(project)
