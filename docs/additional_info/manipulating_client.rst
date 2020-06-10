.. _additional-info:
.. index:: Client

Manipulating client
===================

.. _customizing-client:

Customizing client
------------------

By default, the client will wait indefinitely for a server response.
You may override connect and/or read timeout in the following way:

.. code-block:: python

  import lokalise
  client = lokalise.Client('token', connect_timeout=5, read_timeout=7)

Note that the timeout values are in *seconds*.

Resetting client
----------------

To reset your client, simply use the `reset_client()` method:

.. code-block:: python

  client = lokalise.Client('token', connect_timeout=5, read_timeout=7)
  # do something with the client
  client.reset_client()
  client.token # => None
  client.connect_timeout # => None
  client.read_timeout # => None
