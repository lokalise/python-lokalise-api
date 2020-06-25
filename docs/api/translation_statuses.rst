Translation statuses endpoint
=============================

`Translation statuses documentation <https://app.lokalise.com/api2docs/curl/#resource-translation-statuses>`_

Fetch all translation statuses
------------------------------

.. py:function:: translation_statuses(project_id, [params = None])

  :param str project_id: ID of the project
  :param dict params: (optional) :ref:`pagination options <collections-pagination>`
  :return: Collection of translation statuses

Example:

.. code-block:: python

  statuses = client.translation_statuses('123.abc', {
      "page": 2,
      "limit": 1
  })
  assert statuses.items[0].title == "waiting for approval"

Fetch a translation status
--------------------------

.. py:function:: translation_status(project_id, translation_status_id)

  :param str project_id: ID of the project
  :param translation_status_id: ID of the status to fetch
  :type translation_status_id: int or str
  :return: Translation status model

Example:

.. code-block:: python

  status = client.translation_status('123.abc', 345)
  status.title # => "needs context"
  status.color # => "#61bd4f"

Create translation status
-------------------------

.. py:function:: create_translation_status(project_id, params)

  :param str project_id: ID of the project
  :param dict params: Translation status parameters
  :return: Translation status model

Example:

.. code-block:: python

  status = client.create_translation_status('123.abc', {
      "title": "Python status",
      "color": "#ff9f1a"
  })
  status.title # => "Python status"
  status.color # => "#ff9f1a"

Update translation status
-------------------------

.. py:function:: update_translation_status(project_id, translation_status_id, [params = None])

  :param str project_id: ID of the project
  :param translation_status_id: ID of the status to update
  :type translation_status_id: int or str
  :param dict params: Translation status parameters
  :return: Translation status model

Example:

.. code-block:: python

  status = client.update_translation_status('123.abc', 3456, {
      "title": "Python status updated"
  })
  status.title # => "Python status updated"

Delete translation status
-------------------------

.. py:function:: delete_translation_status(project_id, translation_status_id)

  :param str project_id: ID of the project
  :param translation_status_id: ID of the status to delete
  :type translation_status_id: int or str
  :return: Dict with project ID and `custom_translation_status_deleted`: True

Example:

.. code-block:: python

  client.delete_translation_status('123.abc', 345)

Fetch all available statuses colors
-----------------------------------

.. py:function:: translation_statuses_colors(project_id)

  Fetches available RGB colors that can be assigned to translation statuses.

  :param str project_id: ID of the project
  :return: List with the RGB color codes

Example:

.. code-block:: python

  colors = client.translation_statuses_colors('123.abc')
  colors[0] # => '#61bd4f'
