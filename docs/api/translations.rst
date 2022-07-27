Translations endpoint
=====================

`Translations documentation <https://developers.lokalise.com/reference/list-all-translations>`_

Fetch all translations
----------------------

.. py:function:: translations(project_id, [params = None])

  :param str project_id: ID of the project
  :param dict params: (optional) Request parameters
  :return: Collection of translations

Example:

.. code-block:: python

  translations = client.translations('123.abc', {
      "page": 2,
      "limit": 5,
      "disable_references": 1,
      "filter_untranslated": 1
  })
  translations.items[0].translation_id # => 220681321

Fetch a translation
-------------------

.. py:function:: translation(project_id, translation_id, [params = None])

  :param str project_id: ID of the project
  :param translation_id: ID of the translation to fetch
  :type translation_id: int or str
  :param dict params: (optional) Request parameters
  :return: Task model

Example:

.. code-block:: python

  translation = client.translation('123.abc', 220681321, {
      "disable_references": 1
  })
  translation.translation # => "Welcome to the app!"
  translation.language_iso # => "en_US"
  translation.is_reviewed # => True

Update a translation
--------------------

.. py:function:: update_translation(project_id, translation_id, params)

  :param str project_id: ID of the project
  :param translation_id: ID of the translation to update
  :type translation_id: int or str
  :param dict params: Translation parameters
  :return: Task model

Example:

.. code-block:: python

  translation = client.update_translation(PROJECT_ID, TRANSLATION_ID, {
      "translation": "Welcome again!",
      "custom_translation_status_ids": [429]
  })
  translation.translation # => "Welcome again!"
  translation.custom_translation_statuses[0]['status_id'] # => 429
