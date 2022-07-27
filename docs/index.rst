.. python-lokalise-api documentation master file, created by
   sphinx-quickstart on Wed Jun 10 12:58:50 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Lokalise API v2 Python interface
================================

Official `Lokalise APIv2 <https://developers.lokalise.com/reference/lokalise-rest-api>`_ Python
interface that represents returned data as Python objects.

.. code-block:: python

  import lokalise
  client = lokalise.Client('YOUR_API_TOKEN')
  project = client.project('123.abc')
  print(project.name)

  client.upload_file(project.project_id, {
      "data": 'ZnI6DQogIHRlc3Q6IHRyYW5zbGF0aW9u',
      "filename": 'python_upload.yml',
      "lang_iso": 'en'
  })

  translation_keys = client.keys(project.project_id, {"page": 2,
      "limit": 3,
      "disable_references": "1"})
  translation_keys.items[0].key_name['web'] # => "sign_up"

You can also use `OAuth 2 tokens <https://python-lokalise-api.readthedocs.io/en/latest/additional_info/oauth2_flow.html>`_ and perform requests on the user's behalf:

.. code-block:: python

  client = lokalise.OAuthClient('YOUR_OAUTH2_API_TOKEN')

  project = client.project('123.abc')


Usage
-----

.. toctree::
   :maxdepth: 2

   api/getting_started
   api/branches
   api/comments
   api/contributors
   api/files
   api/keys
   api/languages
   api/orders
   api/payment_cards
   api/projects
   api/queued_processes
   api/snapshots
   api/screenshots
   api/segments
   api/tasks
   api/teams
   api/team_users
   api/team_user_groups
   api/team_user_billing_details
   api/translations
   api/translation_providers
   api/translation_statuses
   api/webhooks

Additional information
----------------------

.. toctree::
  :maxdepth: 1

  additional_info/oauth2_flow
  additional_info/manipulating_client
  additional_info/exception_handling
  additional_info/contributing
  additional_info/changelog
  additional_info/license
