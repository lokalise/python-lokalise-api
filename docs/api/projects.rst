Projects endpoint
=================

`Projects documentation <https://developers.lokalise.com/reference/list-all-projects>`_

Fetch all projects
------------------

.. py:function:: projects([params=None])

  :param dict params: (optional) :ref:`pagination options <collections-pagination>`
  :return: Collection of projects

Example:

.. code-block:: python

  client.projects({"page": 2, "limit": 10})

Fetch a single project
----------------------

.. py:function:: project(project_id)

  :param str project_id: ID of the project to fetch
  :return: Project model

Example:

.. code-block:: python

  project = client.project('123.abc')
  project.project_type # => "localization_files"
  project.name # => "Sample Project"

Create project
--------------

.. py:function:: create_project(params)

  :param dict params: Project parameters
  :return: Project model

Example:

.. code-block:: python

  client.create_project({
      "name": "Python sample project",
      "description": "Project created by Python client",
      "languages": [
          {
              "lang_iso": "en",
              "custom_iso": "en-us"
          },
          {
              "lang_iso": "en_GB",
              "custom_iso": "en-gb"
          }
      ],
      "base_lang_iso": "en-us"
  })

Update project
--------------

.. py:function:: update_project(project_id, params)

  :param str project_id: ID of the project to update
  :param dict params: Project parameters
  :return: Project model

Example:

.. code-block:: python

  client.update_project('123.abc', {
      "name": "Updated Python proj",
      "description": "Proj updated by Python"
  })

Empty project
-------------

.. py:function:: empty_project(project_id)

  Empties a given project by removing all keys and translations.

  :param str project_id: ID of the project to empty
  :return: Dictionary with the project ID and "keys_deleted" set to True
  :rtype dict:

Example:

.. code-block:: python

  client.empty_project('123.abc')

Delete project
--------------

.. py:function:: delete_project(project_id)

  :param str project_id: ID of the project to delete
  :return: Dictionary with the project ID and "project_deleted" set to True
  :rtype dict:

Example:

.. code-block:: python

  client.delete_project('123.abc')
