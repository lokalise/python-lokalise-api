Payment cards endpoint
======================

`Payment cards documentation <https://developers.lokalise.com/reference/list-all-cards>`_

Fetch all payment cards
-----------------------

.. py:function:: payment_cards([params = None])

:param dict params: (optional) :ref:`pagination options <collections-pagination>`
:return: Collection of payment cards

Example:

.. code-block:: python

  client.payment_cards({"page": 2, "limit": 1})

Fetch a payment card
--------------------

.. py:function:: payment_card(payment_card_id)

  :param payment_card_id: ID of the payment card to fetch
  :type payment_card_id: str or int
  :return: Payment card model

Example:

.. code-block:: python

  card = client.payment_card(3456)
  card.last4 # => "8148"
  card.branch # => "MasterCard"

Create a payment card
---------------------

.. py:function:: create_payment_card(params)

  :param dict params: Payment card parameters
  :return: Payment card model

Note that the card will be added to the user identified by the currently used API token.
The card will not be available to any other user, and Lokalise will not store
card details. Once the card is added, its details are sent to Stripe.

Example:

.. code-block:: python

  card = client.create_payment_card({
      "number": "4242424242420391",
      "cvc": 123,
      "exp_month": 9,
      "exp_year": 2025
  })
  card.last4 # => "0391"

Delete payment card
-------------------

.. py:function:: delete_payment_card(payment_card_id)

  :param payment_card_id: ID of the payment card to delete
  :type payment_card_id: int or str
  :return: Dictionary with card ID and "card_deleted" set to True
  :rtype dict:

Example:

.. code-block:: python

  client.delete_payment_card(12345)
