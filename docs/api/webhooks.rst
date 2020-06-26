Webhooks endpoint
=================

`Webhooks documentation <https://app.lokalise.com/api2docs/curl/#resource-webhooks>`_

Fetch all webhooks
------------------

.. py:function:: webhooks(project_id, [params = None])

  :param str project_id: ID of the project
  :param dict params: Pagination parameters
  :return: Webhook collection

Example:

.. code-block:: python

  webhooks = client.webhooks('123.abc', {"page": 2, "limit": 2})
  webhooks.items[0].webhook_id # => "0efe309..."

Fetch a single webhook
----------------------

.. py:function:: webhook(project_id, webhook_id)

  :param str project_id: ID of the project
  :param str webhook_id: ID of the webhook to fetch
  :return: Webhook model

Example:

.. code-block:: python

  webhook = client.webhook('123.abc', "0efe...")
  webhook.url # => "http://example.com/notify"
  webhook.secret # => "xyz345890"

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

Update webhook
--------------

.. py:function:: update_webhook(project_id, webhook_id, [params = None])

  :param str project_id: ID of the project
  :param str webhook_id: ID of the webhook to update
  :param dict params: Webhook parameters
  :return: Webhook model

Example:

.. code-block:: python

  webhook = client.update_webhook('123.abc', "0efe...", {
      "events": ["project.translation.updated"]
  })
  webhook.events # => ["project.translation.updated"]

Delete webhook
--------------

.. py:function:: delete_webhook(project_id, webhook_id)

Example:

.. code-block:: python

  client.delete_webhook('123.abc', "0efe...")

Regenerate webhook secret
-------------------------

.. py:function:: regenerate_webhook_secret(project_id, webhook_id)

  :param str project_id: ID of the project
  :param str webhook_id: ID of the webhook to regenerate secret for
  :return: Dict with project ID and `secret` with the new secret's value

Example:

.. code-block:: python

  resp = client.regenerate_webhook_secret('123.abc', "0efe...")
  resp['secret'] # => "xyz123abc"
