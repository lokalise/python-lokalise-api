JWT endpoint
============

Get OTA JWT
-----------

.. py:function:: jwt()

  :return: JWT model

Example:

.. code-block:: python

  response = client.jwt()
  response.jwt # => "eyJ0eXAiOiJK..."
