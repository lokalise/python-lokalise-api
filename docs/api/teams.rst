Teams endpoint
==============

`Teams documentation <https://app.lokalise.com/api2docs/curl/#resource-teams>`_

Fetch all teams
---------------

.. py:function:: teams([params = None])

  :param dict params: (optional) :ref:`pagination options <collections-pagination>`
  :return: Collection of teams

Example:

.. code-block:: python

  teams = client.teams({"page": 2, "limit": 3})
  teams.items[0].team_id # => 156123
