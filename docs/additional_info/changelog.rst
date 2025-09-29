.. index:: Changelog

Changelog
=========

4.0.0 (29-Sep-2025)
-------------------

* Require Python 3.10+
* Fully rework typing system
* Make code more solid, enhance error handling
* Switch to uv, black, ruff

3.5.1 (14-May-2025)
-------------------

* Added `_response_too_big` param in the `download_files` method for `Current contributor <https://developers.lokalise.com/reference/download-files>`_ endpoint

3.5.0 (08-May-2025)
-------------------

* Added support for `Current contributor <https://developers.lokalise.com/reference/retrieve-me-as-a-contributor>`_ endpoint
* Added support for `Fetch team <https://developers.lokalise.com/reference/get-team-details>`_ endpoint

3.4.0 (30-Apr-2025)
-------------------

* Added `projectId` field for glossary entries

3.3.0 (22-Apr-2025)
-------------------

* Added support for `GlossaryTerms <https://developers.lokalise.com/reference/list-glossary-terms>`_ endpoint:

.. code-block:: python

  glossary_terms = client.glossary_terms(PROJECT_ID, {
    "limit": 2,
  })

  glossary_term = glossary_terms.items[0]
  glossary_term.term # => "router"
  glossary_terms.next_cursor # => "5489103"


  new_glossary_terms = client.create_glossary_terms(PROJECT_ID, [
      {
          "term": "python",
          "description": "sample desc",
          "caseSensitive": False,
          "forbidden": False,
          "translatable": True,
          "tags": ["term1"]
      },
      {
          "term": "code editor",
          "description": "",
          "caseSensitive": False,
          "forbidden": False,
          "translatable": True,
          "translations": [{
              "langId": 674,
              "translation": "éditeur de code",
              "description": (
                  "Logiciel permettant d’écrire, modifier "
                  "et organiser du code informatique."
              )
          }],
          "tags": ["term2"]
      },
  ])

  new_glossary_terms.items[0].term # => "python"


3.2.0 (17-Feb-2025)
-------------------

* Add support for `async file downloads <https://developers.lokalise.com/reference/download-files-async>`_:

.. code-block:: python

  process = client.download_files_async(PROJECT_ID, {
      "format": "json",
      "original_filenames": True,
      "replace_breaks": False
  })

  process_info = client.queued_process(
    PROJECT_ID,
    process.process_id
  )

  process_info.status # => 'finished'

3.1.1 (30-Jan-2025)
-------------------

* Add `is_unverified` to `Translation`

3.1.0 (27-Nov-2024)
-------------------

* Allow to provide a custom API host:

.. code-block:: python

  custom_api_host = "http://example.com/api/"
  client = lokalise.Client(
      "token",
      connect_timeout=5,
      read_timeout=3,
      enable_compression=True,
      api_host=custom_api_host)

3.0.0 (15-Oct-2024)
-------------------

* Drop support for Python 3.8 (EOL), test with Python 3.13
* Added support for `PermissionTemplates` endpoint:

.. code-block:: python

  templates = client.permission_templates(TEAM_ID)
  
  template.id # => 1
  template.role # => "Manager"
  template.permissions # => ['branches_main_modify', ...]
  template.description # => 'Manage project settings ...'
  template.tag # => 'Full access'
  template.tagColor # => 'green'
  template.tagInfo # => ''
  template.doesEnableAllReadOnlyLanguages # => true

* Added `role_id` to the `Contributor` model

.. code-block:: python

  contributor = client.contributor(PROJECT_ID, CONTRIBUTOR_ID)
  contributor.role_id # => 5

* Added `role_id` to the `TeamUserGroup` model

.. code-block:: python

  group = client.team_user_group(TEAM_ID, GROUP_ID)
  group.role_id # => 5

2.3.0 (15-May-2024)
-------------------

* Add support for `cursor pagination <https://python-lokalise-api.readthedocs.io/en/latest/api/getting-started#cursor-pagination>`_ for List keys and List translation endpoints:

.. code-block:: python

  keys = client.keys(YOUR_PROJECT_ID, {
      "limit": 2, # The number of items to fetch. Optional, default is 100
      "pagination": "cursor",
      "cursor": "eyIxIjo0NDU5NjA2MX0=" # The starting cursor. Optional, string
  })

  keys.has_next_cursor() # => True or False
  keys.next_cursor # => String or None

2.2.0 (17-Apr-2024)
-------------------

* Require Python 3.8
* Update dependencies

2.1.2 (09-Aug-2023)
-------------------

* Relaxed typings for `create_webhook` and `update_webhook` to allow passing the necessary parameters

2.1.1 (27-Feb-2023)
-------------------

* Added the `source_language_iso` attribute for the `Task` model (thanks, @MVasquezDXC)
* Updated dependencies

2.1.0 (11-Jan-2023)
-------------------

* Updated the `jwt()` method. To request a JWT, you must provide the project ID:

.. code-block:: python

  response = client.jwt("1234.abcd")
  response.jwt # => "eyJ0eXAiOiJK..."

2.0.0 (09-Dec-2022)
-------------------

* Drop support for Python 3.6
* Switch to Poetry to perform dependency management and build
* Minor updates

1.7.0 (30-Nov-2022)
-------------------

* Added support for the `JWT endpoint <https://developers.lokalise.com/reference/create-service-jwt>`_.

.. code-block:: python

  response = client.jwt()
  response.jwt # => "eyJ0eXAiOiJK..."

1.6.0 (05-Oct-2022)
-------------------

* Added `file_id` attribute to `File` model:

.. code-block:: python

  files = client.files(project_id)
  files.items[0].file_id # => 839819

1.5.0 (07-Jul-2022)
-------------------

* Added support for `Delete file endpoint <https://python-lokalise-api.readthedocs.io/en/latest/api/files.html#delete-file>`_:

.. code-block:: python

  response = client.delete_file(project_id, file_id)
  response['file_deleted'] # => True

1.4.0 (07-Mar-2022)
-------------------

* Added support for OAuth 2 flow. You can now request `OAuth 2 tokens using this client <https://python-lokalise-api.readthedocs.io/en/latest/additional_info/oauth2_flow.html>`_:

.. code-block:: python

  auth_client = lokalise.Auth('client id', 'client secret')
  url = auth_client.auth(["read_projects", "write_team_groups"])
  token_data = auth_client.token('auth code')
  refreshed_token_data = auth_client.refresh('refresh token')

* Do not test with Python 3.6 anymore (EOL)

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
