Queued processes endpoint
=========================

`Queued processes documentation <https://app.lokalise.com/api2docs/curl/#resource-queued-processes>`_

Fetch all queued processes
--------------------------

.. py:function:: queued_processes(project_id)

  :param str project_id: ID of the project
  :return: Collection of queued processes

Example:

.. code-block:: python

  client.queued_processes('123.abc')

.. _queued-process:

Fetch a single queued process
-----------------------------

.. py:function:: queued_process(project_id, queued_process_id)

  :param str project_id: ID of the project
  :param queued_process_id: ID of the process to fetch
  :type queued_process_id: int or str
  :return: Queued process model

Example:

.. code-block:: python

  process = client.queued_process('123.abc', '1234abcf456zyx')
  process.type # => 'file-import'
  process.status # => 'finished'
