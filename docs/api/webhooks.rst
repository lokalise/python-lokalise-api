Webhooks endpoint
=================

`Webhooks documentation <https://app.lokalise.com/api2docs/curl/#resource-webhooks>`_

Fetch all webhooks
------------------

.. py:function::

Example:

.. code-block:: python

Fetch a single webhook
----------------------

.. py:function::

Example:

.. code-block:: python

Create webhook
--------------

.. py:function:: create_webhook(project_id, params)

  :param str project_id: ID of the project
  :param dict params: Webhook parameters
  :return: Webhook model

Example:

.. code-block:: python

  webhook = client.create_webhook('123.abc', {
      "url": r"http://example.com/notify",
      "events": ["project.imported", "project.snapshot"]
  })
  webhook.url # => "http://example.com/notify"
  webhooks.events # => ["project.imported", "project.snapshot"]

Fetch all webhooks
------------------

.. py:function::

Example:

.. code-block:: python

Fetch all webhooks
------------------

.. py:function::

Example:

.. code-block:: python

Fetch all webhooks
------------------

.. py:function::

Example:

.. code-block:: python
