Tasks endpoint
==============

`Tasks documentation <https://app.lokalise.com/api2docs/curl/#resource-tasks>`_

Fetch all tasks
---------------

.. py:function:: tasks(project_id, [params = None])

  :param str project_id: ID of the project
  :param dict params: (optional) Request parameters
  :return: Collection of tasks

Example:

.. code-block:: python

  tasks = client.tasks('123.abc', {
      "page": 2,
      "limit": 3,
      "filter_statuses": "completed"
  })
  tasks.items[0].task_id # => 89334


Fetch a task
------------

.. py:function:: task(project_id, task_id)

  :param str project_id: ID of the project
  :param task_id: ID of the task to fetch
  :type task_id: int or str
  :return: Task model

Example:

.. code-block:: python

  task = client.task('123.abc', 89334)
  task.task_id # => 89334
  task.title # => "Demo task"


Create a task
-------------

.. py:function:: create_task(project_id, params)

  :param str project_id: ID of the project
  :param dict params: Task parameters
  :return: Task model

Example:

.. code-block:: python

  task = client.create_task('123.abc', {
      "title": "Python task",
      "languages": [{
          "language_iso": "en",
          "users": [203]
      }],
      "keys": [340891],
      "auto_close_task": True
  })
  task.project_id # => '123.abc'
  task.title # => "Python task"
  task.languages[0]['language_iso'] # => "en"
  task.auto_close_task # => True


Update a task
-------------

.. py:function:: update_task(project_id, task_id, [params = None])

  :param str project_id: ID of the project
  :param task_id: ID of the task to update
  :type task_id: int or str
  :param dict params: Task parameters
  :return: Task model

Example:

.. code-block:: python

  task = client.update_task('123.abc', 34567, {
      "title": "Python updated task",
      "due_date": "2020-08-24 23:59:59"
  })
  task.title # => "Python updated task"
  task.due_date # => "2020-08-24 21:59:59 (Etc/UTC)"

Delete a task
-------------

.. py:function:: delete_task(project_id, task_id)

  :param str project_id: ID of the project
  :param task_id: ID of the task to delete
  :type task_id: int or str
  :return: Dictionary with the project ID and "task_deleted": True

Example:

.. code-block:: python

  client.delete_task('123.abc', 34567)
