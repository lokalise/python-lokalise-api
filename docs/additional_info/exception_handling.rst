.. index:: Exception handling

Exception handling
==================

`Learn more about error codes in the official doc <https://developers.lokalise.com/reference/api-errors>`_.

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
* ``lokalise.errors.TooManyRequests`` (429) - too many requests hit the API too quickly (check the section below to learn more).
* ``lokalise.errors.ServerError`` (500).
* ``lokalise.errors.BadGateway`` (502).
* ``lokalise.errors.ServiceUnavailable`` (503).
* ``lokalise.errors.GatewayTimeout`` (504).

To handle an exception you would do the following:

.. code-block:: python

    try:
        project = client.project("invalid")
    except errors.BadRequest as e:
        print("=== Lokalise API Error ===")
        print("Type:", type(e).__name__)
        print("Status code:", e.status_code)
        print("Message:", e.message)
        print("Headers:", e.headers)
        print("Raw text:", e.raw_text)

        if e.parsed:
            print("--- Parsed error ---")
            print("Parsed status:", e.parsed.status)
            print("Parsed message:", e.parsed.message)
            print("Parsed reason:", e.parsed.reason)
            print("Parsed code:", e.parsed.code)
            print("Parsed details:", e.parsed.details)

Rate limits
-----------

Access to all endpoints is limited to 6 requests per second from 14 September, 2021. This limit is applied per API token and per IP address. If you exceed the limit, a 429 HTTP status code will be returned and the corresponding exception will be raised that you should handle properly. To handle such errors, we recommend an exponential backoff mechanism with a limited number of retries.