Screenshots endpoint
====================

`Screenshots documentation <https://developers.lokalise.com/reference/list-all-screenshots>`_

Fetch all screenshots
---------------------

.. py:function:: screenshots(project_id, [params = None])

  :param str project_id: ID of the project
  :param dict params: :ref:`pagination options <collections-pagination>`
  :return: Collection of screenshots

Example:

.. code-block:: python

  client.screenshots('123.abc', {"page": 2, "limit": 3})

Fetch a screenshot
------------------

.. py:function:: screenshot(project_id, screenshot_id)

  :param str project_id: ID of the project
  :param screenshot_id: ID of the screenshot to fetch
  :type screenshot_id: int or str
  :return: Screenshot model

Example:

.. code-block:: python

  screenshot = client.screenshot('123.abc', 12345)
  screenshot.width # => 480
  screenshot.height # => 800

Create screenshots
------------------

.. py:function:: create_screenshots(project_id, params)

  :param str project_id: ID of the project
  :param params: Screenshots parameters
  :type params: dict or list
  :return: Collection of screenshots

Example:

.. code-block:: python

  screenshots = client.create_screenshots('123.abc', [{
      "data": 'data:image/jpeg;base64,iVBOR...',
      "title": "Python screenshot",
      "ocr": False
  }])
  screenshots.items[0].title # => "Python screenshot"

Update a screenshot
-------------------

.. py:function:: update_screenshot(project_id, screenshot_id, [params = None])

  :param str project_id: ID of the project
  :param screenshot_id: ID of the screenshot to update
  :type screenshot_id: int or str
  :param dict params: Screenshots parameters
  :return: Screenshot model

Example:

.. code-block:: python

  screenshot = client.update_screenshot('123.abc', 12345, {
      "title": "Updated by Python",
      "description": "Python description"
  })
  screenshot.title # => "Updated by Python"

Delete a screenshot
-------------------

.. py:function:: delete_screenshot(project_id, screenshot_id)

  :param str project_id: ID of the project
  :param screenshot_id: ID of the screenshot to delete
  :type screenshot_id: int or str
  :return: Dictionary with the project ID and "screenshot_deleted": True

Example:

.. code-block:: python

  client.delete_screenshot('123.abc', 496094)
