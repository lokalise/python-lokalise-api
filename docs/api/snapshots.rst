Snapshots endpoint
==================

`Snapshots documentation <https://app.lokalise.com/api2docs/curl/#resource-snapshots>`_

Fetch all snapshots
-------------------

.. py:function:: snapshots(project_id, [params = None])

  :param str project_id: ID of the project
  :param dict params: :ref:`pagination options <collections-pagination>`
  :return: Collection of snapshots

Example:

.. code-block:: python

  snapshots = client.snapshots('123.abc', {"page": 2, "limit": 1})
  snapshots.items[0].snapshot_id # => 163512

Create a snapshot
-----------------

.. py:function:: create_snapshot(project_id, [params = None])

  :param str project_id: ID of the project
  :param dict params: (optional) Request params
  :return: Snapshot model

Example:

.. code-block:: python

  snapshot = client.create_snapshot('123.abc', {"title": "Python snapshot"})
  snapshot.title # => "Python snapshot"

Restore a snapshot
------------------

.. py:function:: restore_snapshot(project_id, snapshot_id)

Note that the snapshot will be restored to the project copy, not to the initial project.

Example:

.. code-block:: python

  project = client.restore_snapshot('123.abc', 34567)
  project.project_id != '123.abc' # => True
  project.name # => "MyProject copy"

Delete a snapshot
-----------------

.. py:function:: delete_snapshot(project_id, snapshot_id)

  :param str project_id: ID of the project
  :param snapshot_id: ID of the snapshot to delete
  :return: Dictionary with project ID and "snapshot_deleted" set to True
  :rtype dict:

Example:

.. code-block:: python

  client.delete_snapshot('123.abc', 34567)
