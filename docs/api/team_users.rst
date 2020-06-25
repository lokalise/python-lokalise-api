Team users endpoint
===================

`Team users documentation <https://app.lokalise.com/api2docs/curl/#resource-team-users>`_

Fetch all team users
--------------------

.. py:function:: team_users(team_id, [params = None])

:param team_id: ID of the team
:type team_id: str or int
:param dict params: (optional) :ref:`pagination options <collections-pagination>`
:return: Collection of team users

Example:

.. code-block:: python

  users = client.team_users(7890, {
      "page": 2,
      "limit": 4
  })
  users.items[0].user_id # => 12345

Fetch a team user
-----------------

.. py:function:: team_user(team_id, team_user_id)

  :param team_id: ID of the team
  :type team_id: str or int
  :param team_user_id: ID of the team user to fetch
  :type team_user_id: str or int
  :return: Team user model

Example:

.. code-block:: python

  user = client.team_user(7890, 12345)
  user.email # => "elf@lorien.com"
  user.fullname # => "Mr. Elf"

Update a team user
------------------

.. py:function:: update_team_user(team_id, team_user_id, [params = None])

  :param team_id: ID of the team
  :type team_id: str or int
  :param team_user_id: ID of the team user to update
  :type team_user_id: str or int
  :param dict params: (optional) Team user parameters
  :return: Team user model

Example:

.. code-block:: python

  user = client.update_team_user(7890, 12345, {"role": "admin"})
  user.role # => "admin"

Delete a team user
------------------

.. py:function:: delete_team_user(team_id, team_user_id)

  :param team_id: ID of the team
  :type team_id: str or int
  :param team_user_id: ID of the team user to delete
  :type team_user_id: str or int
  :return: Dict with the team ID and `team_user_deleted` set to True

Example:

.. code-block:: python

  client.delete_team_user(7890, 12345)
