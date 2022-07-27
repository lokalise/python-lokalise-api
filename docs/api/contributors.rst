Contributors endpoint
=====================

`Contributors documentation <https://developers.lokalise.com/reference/list-all-contributors>`_

Fetch all contributors
----------------------

.. py:function:: contributors(project_id, [params=None])

  :param str project_id: ID of the project to fetch contributors for.
  :param dict params: (optional) :ref:`pagination options <collections-pagination>`
  :return: Collection of contributors

Example:

.. code-block:: python

  client.contributors('123.abc', {"limit": 3, "page": 2})

Fetch a single contributor
--------------------------

.. py:function:: contributor(project_id, contributor_id)

  :param str project_id: ID of the project
  :param contributor_id: ID of the contributor to fetch
  :type contributor_id: int or str
  :return: Contributor model

Example:

.. code-block:: python

  contributor = client.contributor('123.abc', 2345)
  contributor.email == "test@example.com"
  contributor.fullname == "John Doe"

Create one or multiple contributors
-----------------------------------

.. py:function:: create_contributors(project_id, params)

  :param str project_id: ID of the project
  :param params: Contributors parameters
  :type params: list or dict
  :return: Contributors collection

Creating multiple contributors example:

.. code-block:: python

  client.create_contributors('123.abc', [
      {
          "email": "demo@python.org",
          "fullname": "Python demo 1",
          "languages": [{
              "lang_iso": "en",
              "is_writable": False
          }]
      },
      {
          "email": "demo2@python.org",
          "fullname": "Python demo 2",
          "languages": [{
              "lang_iso": "en",
              "is_writable": True
          }]
      }
  ])

Creating one contributor:

.. code-block:: python

  client.create_contributors(PROJECT_ID, {
      "email": "demo3@python.org",
      "fullname": "Python demo 3",
      "languages": [{
          "lang_iso": "ru_RU",
          "is_writable": True
      }]
  })

Update contributor
------------------

.. py:function:: update_contributor(project_id, contributor_id, params)

  :param str project_id: ID of the project
  :param contributor_id: ID of the contributor to update
  :type contributor_id: int or str
  :param dict params: Update parameters
  :return: Contributor model

Example:

.. code-block:: python

  client.update_contributor('123.abc', 23456, {
      "is_reviewer": True,
      "languages": [
          {
              "lang_iso": "ru_RU",
              "is_writable": True
          },
          {
              "lang_iso": "en",
              "is_writable": False
          }
      ]
  })

Delete contributor
------------------

.. py:function:: delete_contributor(project_id, contributor_id)

  :param str project_id: ID of the project
  :param contributor_id: ID of the contributor to delete
  :type contributor_id: int or str
  :return: Dictionary with project ID and "contributor_deleted" set to True
  :rtype dict:

Example:

.. code-block:: python

  client.delete_contributor('123.abc', 34567)
