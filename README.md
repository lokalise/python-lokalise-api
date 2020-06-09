# Lokalise API v2 official Python interface

Official Python interface for the Lokalise APIv2.

## Index

* [Getting started](#getting-started)
* [Testing](#testing)
* [Additional info](#additional-info)

## Getting started

Work in progress.

## Additional info

### Setting timeouts

By default, the client will wait indefinitely for a server response. You may override connect and/or read timeout in the following way:

```python
lokalise.Client('token', connect_timeout=5, read_timeout=7)
```

Note that the timeout values are in *seconds*.

### Exception handling

[Learn more about error codes in the official doc](https://app.lokalise.com/api2docs/curl/#resource-errors)

The plugin may raise the following exceptions:

* `lokalise.errors.ClientError` - generic error.
* `lokalise.errors.BadRequest` (400) - the provided request incorrect.
* `lokalise.errors.Unauthorized` (401) - token is missing or incorrect.
* `lokalise.errors.Forbidden` (403) - authenticated user does not have sufficient rights to perform the desired action.
* `lokalise.errors.NotFound` (404) - the provided endpoint (resource) cannot be found.
* `lokalise.errors.MethodNowAllowed` (405) - HTTP request with the provided verb is not supported by the endpoint.
* `lokalise.errors.NotAcceptable` (406) - posted resource is malformed.
* `lokalise.errors.Conflict` (409) - request conflicts with another request.
* `lokalise.errors.Locked` (423) - your token is used simultaneously in multiple requests.
* `lokalise.errors.TooManyRequests` (429).
* `lokalise.errors.ServerError` (500).
* `lokalise.errors.BadGateway` (502).
* `lokalise.errors.ServiceUnavailable` (503).
* `lokalise.errors.GatewayTimeout` (504).

To handle an exception you would do the following:

```python
try:
    client.project('invalid_id')
except lokalise.errors.NotFound as err:
    print(err.message)
    print(err.code)
```

## Testing

1. Copypaste `.env.example` file as .env.
2. Put your API token inside. The .env file is excluded from version control so your token is safe. All in all, we use pre-recorded VCR cassettes, so the actual API requests won't be sent.
3. Run `pytest`. Observe test results and coverage. All your tests will be linted automatically.

## License

This plugin is licensed under the MIT License.

Copyright (c) [Lokalise team](https://lokalise.com), [Ilya Bodrov](http://bodrovis.tech)
