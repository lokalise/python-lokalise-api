Translation providers endpoint
==============================

`Translation providers documentation <https://app.lokalise.com/api2docs/curl/#resource-translation-providers>`_

Fetch all translation providers
-------------------------------

.. py:function:: translation_providers(team_id, [params = None])

  :param team_id: ID of the team
  :type team_id: str or int
  :param dict params: (optional) :ref:`pagination options <collections-pagination>`
  :return: Collection of translation providers

Example:

.. code-block:: python

  providers = client.translation_providers(1234, {
      "page": 2,
      "limit": 1
  })
  providers.items[0].name # => "Lokalise"

Fetch a translation provider
----------------------------

.. py:function:: translation_provider(team_id, translation_provider_id)

  :param team_id: ID of the team
  :type team_id: str or int
  :param translation_provider_id: ID of the translation provider to fetch
  :type translation_provider_id: str or int
  :return: Translation provider model

Example:

.. code-block:: python

  provider = client.translation_provider(1234, 4)
  provider.name # => "Lokalise"
  provider.price_pair_min # => "10.00"
