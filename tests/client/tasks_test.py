"""
Tests for the Tasks endpoint.
"""

import pytest


PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
NEW_TASK_ID = 135506

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
    tasks = client.tasks(PROJECT_ID, {
        "page": 2,
        "limit": 3,
        "filter_statuses": "completed"
    })
    assert tasks.project_id == PROJECT_ID
    assert tasks.items[0].task_id == 89364
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
    task = client.task(PROJECT_ID, 89364)
    assert task.project_id == PROJECT_ID
    assert task.task_id == 89364
    assert task.title == "Review English"
    assert task.description == "Typical task to be used as a template"
    assert task.status == "completed"
    assert task.progress == 0
    assert task.due_date == "2020-04-23 22:00:00 (Etc/UTC)"
    assert task.due_date_timestamp == 1587679200
    assert not task.can_be_parent
    assert task.task_type == "review"
    assert not task.parent_task_id
    assert task.closing_tags == []
    assert task.keys_count == 7
    assert task.words_count == 20
    assert task.created_at == "2020-03-25 13:39:06 (Etc/UTC)"
    assert task.created_at_timestamp == 1585143546
    assert task.created_by == 20181
    assert task.created_by_email == "bodrovis@protonmail.com"
    assert task.languages[0]['language_iso'] == "en_AU"
    assert not task.auto_close_languages
    assert not task.auto_close_task
    assert task.completed_at == "2020-04-02 14:37:17 (Etc/UTC)"
    assert task.completed_at_timestamp == 1585838237
    assert task.completed_by == 20181
    assert task.completed_by_email == "bodrovis@protonmail.com"
    assert task.do_lock_translations
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
