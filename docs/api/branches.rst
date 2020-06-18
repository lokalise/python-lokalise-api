Branches endpoint
=================

`Branches documentation <https://app.lokalise.com/api2docs/curl/#resource-branches>`_

Fetch all branches
------------------

.. py:function:: branches(self, project_id: str, [params=None])

  :param str project_id: ID of the project to fetch branches for.
  :param dict params: (optional) Pagination params
  :return: Collection of branches

Example:

.. code-block:: python

  client.branches('123.abc')

Fetch a single branch
---------------------

.. py:function:: branch(project_id, branch_id)

  :param str project_id: ID of the project
  :param branch_id: ID of the branch to fetch
  :type branch_id: int or str
  :return: Branch model

Example:

.. code-block:: python

  client.branch('123.abc', 34567)
