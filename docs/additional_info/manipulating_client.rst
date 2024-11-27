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

You can also enable gzip compression by setting the `enable_compression` option to `True`:

.. code-block:: python

  client = lokalise.Client('token', connect_timeout=5, read_timeout=7, enable_compression=True)

It's also possible to use a different API host:

.. code-block:: python
  
  custom_api_host = "http://example.com/api/"
  client = lokalise.Client(
      "token",
      connect_timeout=5,
      read_timeout=3,
      enable_compression=True,
      api_host=custom_api_host)

Resetting client
----------------

To reset your client, simply use the `reset_client()` method:

.. code-block:: python

  client = lokalise.Client('token', connect_timeout=5, read_timeout=7, enable_compression=True)
  # do something with the client
  client.reset_client()
  client.token # => ''
  client.connect_timeout # => None
  client.read_timeout # => None
  client.enable_compression # => False
