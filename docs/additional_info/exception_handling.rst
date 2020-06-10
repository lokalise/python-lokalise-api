Exception handling
==================

`Learn more about error codes in the official doc <https://app.lokalise.com/api2docs/curl/#resource-errors>`_.

The plugin may raise the following exceptions:

* ``lokalise.errors.ClientError`` - generic error.
* ``lokalise.errors.BadRequest`` (400) - the provided request is incorrect, often due to missing a required parameter.
* ``lokalise.errors.Unauthorized`` (401) - API token is incorrect.
* ``lokalise.errors.Forbidden`` (403) - authenticated user does not have sufficient rights to perform the desired action.
* ``lokalise.errors.NotFound`` (404) - the provided endpoint (resource) cannot be found.
* ``lokalise.errors.MethodNowAllowed`` (405) - HTTP request with the provided verb is not supported by the endpoint.
* ``lokalise.errors.NotAcceptable`` (406) - posted resource is malformed.
* ``lokalise.errors.Conflict`` (409) - request conflicts with another request.
* ``lokalise.errors.Locked`` (423) - your token is used simultaneously in multiple requests.
* ``lokalise.errors.TooManyRequests`` (429) - too many requests hit the API too quickly.
* ``lokalise.errors.ServerError`` (500).
* ``lokalise.errors.BadGateway`` (502).
* ``lokalise.errors.ServiceUnavailable`` (503).
* ``lokalise.errors.GatewayTimeout`` (504).

To handle an exception you would do the following:

.. code-block:: python

  try:
      client.project('invalid_id')
  except lokalise.errors.NotFound as err:
      print(err.message)
      print(err.code)


Rate limits
-----------

Lokalise does not rate-limit requests to the API, however retain a right to
decline the service in case of excessive use
Please note that only one concurrent request per token is allowed.
To ensure data consistency, it is not recommended to access the same project
simultaneously using multiple tokens.
