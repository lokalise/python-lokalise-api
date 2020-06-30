Languages endpoint
==================

`Languages documentation <https://app.lokalise.com/api2docs/curl/#resource-languages>`_

Fetch all system languages
--------------------------

.. py:function:: system_languages([params=None])

  Fetches all languages that Lokalise supports.

  :param dict params: (optional) :ref:`pagination options <collections-pagination>`
  :return: Collection of languages

Example:

.. code-block:: python

  client.system_languages({"page": 2, "limit": 10})

Fetch all project languages
---------------------------

.. py:function:: project_languages(project_id, [params=None])

  Fetches all languages for the given project.

  :param str project_id: ID of the project
  :param dict params: (optional) :ref:`pagination options <collections-pagination>`
  :return: Collection of languages

Example:

.. code-block:: python

  client.project_languages('123.abc', {"page": 2, "limit": 3})

Create project languages
------------------------

.. py:function:: create_languages(project_id, params)

  Create one or more languages for the given project.

      :param str project_id: ID of the project
      :param params: Language parameters
      :type params: dict or list
      :return: Collection of languages

Example:

.. code-block:: python

  client.create_languages('123.abc', [
      {
          "lang_iso": "ar",
          "custom_name": "Custom AR"
      },
      {
          "lang_iso": "be_BY",
          "custom_iso": "by_2"
      }
  ])

Fetch a single project language
-------------------------------

.. py:function:: language(project_id, language_id)

  :param str project_id: ID of the project
  :param language_id: ID of the language to fetch
  :return: Language model

Example:

.. code-block:: python

  language = client.language('123.abc', 345)
  language.lang_iso # => 'lv'
  language.is_rtl # => False

Update project language
-----------------------

.. py:function:: update_language(project_id, language_id, params)

  :param str project_id: ID of the project
  :param language_id: ID of the language to update
  :param dict params: Update parameters
  :return: Language model

Example:

.. code-block:: python

  client.update_language('123.abc', 345, {
      "lang_name": "My very own name"
  })

Delete project language
-----------------------

.. py:function:: delete_language(project_id, language_id)

  :param str project_id: ID of the project
  :param language_id: ID of the language to delete
  :return: Dictionary with project ID and "language_deleted" set to True
  :rtype dict:

Example:

.. code-block:: python

  client.delete_language('123.abc', 345)
