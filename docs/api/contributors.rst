Contributors endpoint
=====================

`Contributors documentation <https://app.lokalise.com/api2docs/curl/#resource-contributors>`_

Fetch all contributors
----------------------

.. code-block:: python

  client.contributors(project_id)

Arguments:

* ``project_id`` (string, required)
* Common :ref:`pagination options <collections-pagination>`

Returns a collection of contributors.

Fetch a single contributor
--------------------------

.. code-block:: python

  client.contributor(project_id, contributor_id)

Arguments:

* ``project_id`` (string, required)
* ``contributor_id`` (string or integer, required)

Returns a contributor model.
