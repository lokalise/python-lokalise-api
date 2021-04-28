"""
Tests for the Tasks endpoint.
"""

import pytest


PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
ANOTHER_PROJECT_ID = "803826145ba90b42d5d860.46800099"
NEW_TASK_ID = 135506
ANOTHER_TASK_ID = 10001


@pytest.mark.vcr
def test_tasks(client):
    """Tests fetching of all tasks
    """
    tasks = client.tasks(PROJECT_ID)
    assert tasks.project_id == PROJECT_ID
    assert tasks.items[0].task_id == 133225


@pytest.mark.vcr
def test_tasks_pagination(client):
    """Tests fetching of all tasks with pagination
    """
    tasks = client.tasks(ANOTHER_PROJECT_ID, {
        "page": 2,
        "limit": 3,
        "filter_statuses": "completed"
    })
    assert tasks.project_id == ANOTHER_PROJECT_ID
    assert tasks.items[0].task_id == ANOTHER_TASK_ID
    assert tasks.current_page == 2
    assert tasks.total_count == 5
    assert tasks.page_count == 2
    assert tasks.limit == 3

    assert tasks.is_last_page()
    assert not tasks.is_first_page()
    assert not tasks.has_next_page()
    assert tasks.has_prev_page()


@pytest.mark.vcr
def test_task(client):
    """Tests fetching of a task
    """
    task = client.task(ANOTHER_PROJECT_ID, ANOTHER_TASK_ID)
    assert task.project_id == ANOTHER_PROJECT_ID
    assert task.task_id == ANOTHER_TASK_ID
    assert task.title == "My new task"
    assert task.description == "Description is here"
    assert task.status == "completed"
    assert task.progress == 0
    assert task.due_date == "2019-04-29 22:00:00 (Etc/UTC)"
    assert task.due_date_timestamp == 1556575200
    assert not task.can_be_parent
    assert task.task_type == "translation"
    assert not task.parent_task_id
    assert task.closing_tags == ["finalized"]
    assert task.keys_count == 2
    assert task.words_count == 16
    assert task.created_at == "2019-04-17 13:44:00 (Etc/UTC)"
    assert task.created_at_timestamp == 1555508640
    assert task.created_by == 20181
    assert task.created_by_email == "bodrovis@protonmail.com"
    assert task.languages[0]['language_iso'] == "es"
    assert task.auto_close_languages
    assert task.auto_close_task
    assert task.auto_close_items
    assert task.completed_at == "2019-10-01 11:14:10 (Etc/UTC)"
    assert task.completed_at_timestamp == 1569928450
    assert task.completed_by == 20181
    assert task.completed_by_email == "bodrovis@protonmail.com"
    assert not task.do_lock_translations
    assert task.custom_translation_status_ids == []


@pytest.mark.vcr
def test_create_task(client):
    """Tests creation of a task
    """
    task = client.create_task(PROJECT_ID, {
        "title": "Python task",
        "languages": [{
            "language_iso": "en",
            "users": [20181]
        }],
        "keys": [34089721],
        "auto_close_task": True
    })
    assert task.project_id == PROJECT_ID
    assert task.task_id == NEW_TASK_ID
    assert task.title == "Python task"
    assert task.languages[0]['language_iso'] == "en"
    assert task.auto_close_task


@pytest.mark.vcr
def test_update_task(client):
    """Tests updating of a task
    """
    task = client.update_task(PROJECT_ID, NEW_TASK_ID, {
        "title": "Python updated task",
        "due_date": "2020-08-24 23:59:59"
    })
    assert task.project_id == PROJECT_ID
    assert task.task_id == NEW_TASK_ID
    assert task.title == "Python updated task"
    assert task.due_date == "2020-08-24 21:59:59 (Etc/UTC)"


@pytest.mark.vcr
def test_delete_task(client):
    """Tests deletion of a task
    """
    resp = client.delete_task(PROJECT_ID, NEW_TASK_ID)
    assert resp['project_id'] == PROJECT_ID
    assert resp['task_deleted']
