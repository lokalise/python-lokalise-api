Orders endpoint
===============

`Orders documentation <https://developers.lokalise.com/reference/list-all-orders>`_

Fetch all orders
----------------

.. py:function:: orders(team_id, [params = None])

  :param team_id: ID of the team
  :type team_id: int or str
  :param dict params: (optional) Pagination params
  :return: Collection of orders

Example:

.. code-block:: python

  client.orders(12345, {"page": 3, "limit": 2})

Fetch a single order
--------------------

.. py:function:: order(team_id, order_id)

  :param team_id: ID of the team
  :type team_id: int or str
  :param str order_id: ID of the order
  :return: Order model

Example:

.. code-block:: python

  order = client.order(12345, "20201102FTR")
  order.status # => "completed"
  order.provider_slug # => "gengo"

Create an order
---------------

.. py:function:: create_order(team_id, params)

  :param team_id: ID of the team
  :type team_id: int or str
  :param dict params: Order parameters
  :return: Order model

Example:

.. code-block:: python

  order = client.create_order(34567, {
      "project_id": '132.abc',
      "card_id": 2185,
      "briefing": "Please make it gooood!",
      "source_language_iso": "en",
      "target_language_isos": ["ru_RU"],
      "keys": [34089123, 3214567],
      "provider_slug": "gengo",
      "translation_tier": 1
  })
  order.project_id # => '132.abc'
  order.card_id # => 2185
  order.status # => "in progress"
  order.provider_slug # => "gengo"
  order.briefing # => "Please make it gooood!"
  order.total # => 1.42
