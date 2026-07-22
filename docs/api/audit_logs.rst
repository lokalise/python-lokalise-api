Audit logs endpoint
=====================

`Audit logs documentation <https://developers.lokalise.com/reference/list-audit-logs>`_

.. important::

This endpoint is only available through :class:`lokalise.ClientV1`.
It is not supported by the standard :class:`lokalise.Client`.

Initialize the client as follows:

.. code-block:: python

  import lokalise

  client = lokalise.ClientV1("YOUR_API_TOKEN")

Fetch audit logs
----------------

.. py:function:: audit_logs(self, [params=None])

  :param dict params: (optional) Pagination and filtering parameters.
  :return: Collection of audit log events.

Example:

.. code-block:: python

  audit_logs = client.audit_logs({
    "limit": 100,
    "event_type": "project.deleted",
  })

  audit_logs.items[0].metadata["event_code"]  # => "project.deleted"
  audit_logs.has_more # => True
  audit_logs.next_cursor # => "some cursor"
  audit_logs.has_next_cursor() # => True
  audit_logs.is_last_page() # => False

To fetch the next set of results, pass `next_cursor` as the `cursor` parameter:

.. code-block:: python

  next_audit_logs = client.audit_logs({
    "limit": 100,
    "cursor": audit_logs.next_cursor,
  })
