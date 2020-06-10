Projects endpoint
=================

`Projects documentation <https://app.lokalise.com/api2docs/curl/#resource-projects>`_

Fetch all projects
------------------

.. code-block:: python

  client.projects()

Arguments:

* Common :ref:`pagination options <collections-pagination>`

Returns a collection of projects.

Fetch a single project
----------------------

.. code-block:: python

  client.project(project_id)

Arguments:

* ``project_id`` (string, required)

Returns a project model.
