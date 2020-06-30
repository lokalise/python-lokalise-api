Team user groups endpoint
=========================

`Team user groups documentation <https://app.lokalise.com/api2docs/curl/#resource-team-user-groups>`_

Fetch all team user groups
--------------------------

.. py:function:: team_user_groups(team_id, [params = None])

  :param team_id: ID of the team
  :type team_id: str or int
  :param dict params: (optional) Pagination parameters
  :return: Collection of team user groups

Example:

.. code-block:: python

  groups = client.team_user_groups(7890, {
      "page": 2,
      "limit": 1
  })
  groups.items[0].group_id # => 1266

Fetch a team user group
-----------------------

.. py:function:: team_user_group(team_id, team_user_group_id)

  :param team_id: ID of the team
  :type team_id: str or int
  :param team_user_group_id: ID of the team user group to fetch
  :type team_user_group_id: str or int
  :return: Team user group model

Example:

.. code-block:: python

  group = client.team_user_group(7890, 123)
  group.name # => "Demo"
  group.permissions['is_admin'] # => True

Create a team user group
------------------------

.. py:function:: create_team_user_group(team_id, params)

  :param team_id: ID of the team
  :type team_id: str or int
  :param dict params: Team user group parameters
  :return: Team user group model

Example:

.. code-block:: python

  group = client.create_team_user_group(7890, {
      "name": "Python group",
      "is_reviewer": True,
      "is_admin": True,
      "admin_rights": ["upload"]
  })
  group.name # => "Python group"
  group.permissions['admin_rights'] # => ["upload"]

Update team user group
----------------------

.. py:function:: update_team_user_group(team_id, team_user_group_id, params)

  :param team_id: ID of the team
  :type team_id: str or int
  :param team_user_group_id: ID of the team user group to update
  :type team_user_group_id: str or int
  :param dict params: Team user group parameters
  :return: Team user group model

Example:

.. code-block:: python

  group = client.update_team_user_group(7890, 123, {
      "name": "Updated Python group",
      "is_reviewer": False,
      "is_admin": True,
      "admin_rights": ["upload"]
  })
  group.name # => "Updated Python group"

Delete team user group
----------------------

.. py:function:: delete_team_user_group(team_id, team_user_group_id)

Example:

.. code-block:: python

  client.delete_team_user_group(7890, 123)

Add projects to a group
-----------------------

.. py:function:: add_projects_to_group(team_id, team_user_group_id, params)

  :param team_id: ID of the team
  :type team_id: str or int
  :param team_user_group_id: ID of the team user group to add projects to
  :type team_user_group_id: str or int
  :param params: Project IDs to add to the group
  :type params: list or str
  :return: Team user group model

Example:

.. code-block:: python

  group = client.add_projects_to_group(7890, 123, ["123.abc", "345.def"])
  "345.def" in group.projects # => True

Remove projects from a group
----------------------------

.. py:function:: remove_projects_from_group(team_id, team_user_group_id, params)

  :param team_id: ID of the team
  :type team_id: str or int
  :param team_user_group_id: ID of the team user group to remove projects from
  :type team_user_group_id: str or int
  :param params: Project IDs to remove from the group
  :type params: list or str
  :return: Team user group model

Example:

.. code-block:: python

  group = client.remove_projects_from_group(7890, 123, ["123.abc", "345.def"])
  "345.def" not in group.projects # => True

Add members to a group
----------------------

.. py:function:: add_members_to_group(team_id, team_user_group_id, params)

  :param team_id: ID of the team
  :type team_id: str or int
  :param team_user_group_id: ID of the team user group to add members to
  :type team_user_group_id: str or int
  :param params: User IDs to add to the group
  :type params: list or str
  :return: Team user group model

Example:

.. code-block:: python

  group = client.add_members_to_group(7890, 123, [421, 187])
  421 in group.members # => True

Remove members from a group
---------------------------

.. py:function:: remove_members_from_group(team_id, team_user_group_id, params)

  :param team_id: ID of the team
  :type team_id: str or int
  :param team_user_group_id: ID of the team user group to remove members from
  :type team_user_group_id: str or int
  :param params: User IDs to remove from the group
  :type params: list or str
  :return: Team user group model

Example:

.. code-block:: python

  group = client.remove_members_from_group(7890, 123, [421, 187])
  421 not in group.members # => True
