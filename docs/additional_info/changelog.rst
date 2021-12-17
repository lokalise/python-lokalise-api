.. index:: Changelog

Changelog
=========

1.3.0 (17-Dec-2021)
-------------------

* Added support for `TeamUserBillingDetails endpoint <https://python-lokalise-api.readthedocs.io/en/latest/api/team_user_billing_details.html>`_
* Added support for `Segments endpoint <https://python-lokalise-api.readthedocs.io/en/latest/api/segments.html>`_

1.2.0 (27-Oct-21)
-----------------

* Add ability to use `OAuth 2 tokens <https://docs.lokalise.com/en/articles/5574713-oauth-2>`_ instead of API tokens obtained from Lokalise profile.

.. code-block:: python

  client = lokalise.OAuthClient('YOUR_OAUTH2_API_TOKEN')

  project = client.project('123.abc')

1.1.1 (21-Sep-21)
-----------------

* Fixed an issue with exception handling when the returned response doesn't contain an `error` key
* Update dependencies

1.1.0 (15-Jul-21)
-----------------

* Added support for gzip compression. It's off by default but you can enable it by setting the `enable_compression` option to `True`:

.. code-block:: python

  client = lokalise.Client('token', connect_timeout=5, read_timeout=7, enable_compression=True)

1.0.0 (29-Apr-21)
-----------------

* The plugin is being actively used for nearly a year, the code is fully reviewed therefore we now consider it to be stable and the first 1.x version is now live. No breaking changes were introduced in this release.

0.4.0 (28-Apr-21)
-----------------

* Add `task_id` attribute to `Translation`

0.3.0 (01-Mar-21)
-----------------

* Add `payment_method` attribute to `Order`

0.2.0 (02-Feb-21)
-----------------

* Add `auto_close_items` attribute for `Task`
* Update all dependencies

0.1.1 (22-Dec-20)
-----------------

* Update all dependencies
* Test against Python 3.9

0.1.0 (30-Jun-20)
-----------------

* Initial release
