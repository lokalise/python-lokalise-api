JWT endpoint
============

Get OTA JWT
-----------

.. py:function:: jwt(project_id, [params = {"service": "ota"}])

  :return: JWT model

Example:

.. code-block:: python

  response = client.jwt("1234.abcd")
  response.jwt # => "eyJ0eXAiOiJK..."
