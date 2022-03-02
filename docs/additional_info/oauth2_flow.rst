.. index:: OAuth 2 flow

OAuth 2 flow
============

You can use this library to request `OAuth 2 tokens <https://docs.lokalise.com/en/articles/5574713-oauth-2>`_ and perform requests on user's behalf.

First, inititalize the client:

.. code-block:: python

  import lokalise

  auth_client = lokalise.Auth('client id', 'client secret')

Pass your client ID and client secret when instantiating the `Auth` class.

Generating OAuth 2 URL
----------------------

Next you'll need to generate a special authentication URL:

.. code-block:: python

  url = auth_client.auth(
      ["read_projects", "write_team_groups"], "http://example.com", '123abc'
  )

At the very least you must provide the first argument which contains the required scopes.

.. py:function:: auth(scope, [redirect_uri = None, state = None])

  :param scope: Requested OAuth scope or scopes
  :type scope: list or str
  :param str redirect_uri: (optional) Redirect URI
  :param str state: (optional) A random string to protect from CSRF attacks

Please note that your users must visit the generated URL and explicitly permit access. As a result, they'll get an authentication code that you'll need on the next step.

Requesting OAuth 2 token
------------------------

Now that you have an authentication code, use it to obtain an OAuth 2 token:

.. code-block:: python

  auth_client.token('auth code')

Pass the authentication code obtained on the previous step.

.. py:function:: token(code)

  :param code: Code obtained with the `auth` method

After running this method you'll get a dict with your access token, refresh token, expiration date, and other information.

Refreshing OAuth 2 token
------------------------

OAuth 2 tokens have expiration dates but you can refresh them using refresh token obtained on the previous step:

.. code-block:: python

  auth_client.refresh('refresh token')

After running this method you'll get a dict with a new access token and other information.

.. py:function:: refresh(refresh_token)

  :param refresh_token: Refresh token obtained with the `token` method

Using OAuth 2 tokens
--------------------

Once you have obtained an access token, you can use it to send requests on the user's behalf:

.. code-block:: python

  client = lokalise.OAuthClient('YOUR_OAUTH2_API_TOKEN')

  project = client.project('123.abc')