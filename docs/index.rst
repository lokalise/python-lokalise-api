.. python-lokalise-api documentation master file, created by
   sphinx-quickstart on Wed Jun 10 12:58:50 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Lokalise API v2 Python client
=============================

Official `Lokalise APIv2 <https://app.lokalise.com/api2docs/curl/>`_ Python
interface that represents returned data as Python objects.

.. code-block:: python

  import lokalise
  client = lokalise.Client('YOUR_API_TOKEN')
  project = client.project('123.abc')
  print(project.title)

  client.upload_file(project.project_id, {
      "data": 'ZnI6DQogIHRlc3Q6IHRyYW5zbGF0aW9u',
      "filename": 'python_upload.yml',
      "lang_iso": 'en'
  })

  translation_keys = client.keys(project.project_id, {"page": 2,
      "limit": 3,
      "disable_references": "1"})
  translation_keys.items[0].key_name['web'] # => "sign_up"

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
   api/teams

Additional information
----------------------

.. toctree::
  :maxdepth: 2

  additional_info/manipulating_client
  additional_info/exception_handling
  additional_info/contributing
  additional_info/changelog
  additional_info/license
