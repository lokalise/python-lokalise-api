Branches endpoint
=================

`Branches documentation <https://developers.lokalise.com/reference/list-all-branches>`_

Fetch all branches
------------------

.. py:function:: branches(self, project_id: str, [params=None])

  :param str project_id: ID of the project to fetch branches for.
  :param dict params: (optional) Pagination params
  :return: Collection of branches

Example:

.. code-block:: python

  branches = client.branches('123.abc')
  branches.items[0].branch_id # => 3456

Fetch a single branch
---------------------

.. py:function:: branch(project_id, branch_id)

  :param str project_id: ID of the project
  :param branch_id: ID of the branch to fetch
  :type branch_id: int or str
  :return: Branch model

Example:

.. code-block:: python

  branch = client.branch('123.abc', 34567)
  branch.name # => "deutch"
  branch.created_at # => "2020-04-03 14:41:46 (Etc/UTC)"

Create a branch
---------------

.. py:function:: create_branch(project_id, params)

  :param str project_id: ID of the project
  :param dict params: Branch parameters
  :return: Branch model

Example:

.. code-block:: python

  branch = client.create_branch('123.abc', {"name": "python-branch"})
  branch.name # => "python-branch"

Update a branch
---------------

.. py:function:: update_branch(project_id, branch_id, params)

  :param str project_id: ID of the project
  :param branch_id: ID of the branch to update
  :type branch_id: int or str
  :param dict params: Update parameters
  :return: Branch model

Example:

.. code-block:: python

  branch = client.update_branch('123.abc', 34567, {"name": "python-branch-updated"})
  branch.name # => "python-branch-updated"


Delete a branch
----------------

.. py:function:: delete_branch(project_id, branch_id)

  :param str project_id: ID of the project
  :param branch_id: ID of the branch to delete
  :type branch_id: int or str
  :return: Dictionary with project ID and "branch_deleted" set to True
  :rtype dict:

Example:

.. code-block:: python

  client.delete_branch('123.abc', 34567)

Merge a branch
--------------

.. py:function:: merge_branch(project_id, branch_id, [params = None])

  :param str project_id: ID of the project
  :param branch_id: ID of the source branch
  :type branch_id: int or str
  :param dict params: Merge parameters
  :return: Dictionary with project ID, "branch_merged" set to True, and branches info stored under the "branch" and "target_branch" keys
  :rtype dict:

Example:

.. code-block:: python

  result = client.merge_branch('123.abc', 34567, {"force_conflict_resolve_using": "target"})
  result['branch'].branch_id # => 34567
  result['branch'].name # => "python-branch"
  result['target_branch'].name # => "master"
