Teams endpoint
==============

`Teams documentation <https://developers.lokalise.com/reference/list-all-teams>`_

Fetch all teams
---------------

.. py:function:: teams([params = None])

  :param dict params: (optional) :ref:`pagination options <collections-pagination>`
  :return: Collection of teams

Example:

.. code-block:: python

  teams = client.teams({"page": 2, "limit": 3})
  teams.items[0].team_id # => 156123


Fetch a single team
-------------------

.. py:function:: team(team_id)

  :param team_id: ID of the team to fetch
  :type team_id: int or str
  :return: Team model

Example:

.. code-block:: python

  team = client.team(12345)
  
  team.team_id # => 12345
  team.name # => "My Team"