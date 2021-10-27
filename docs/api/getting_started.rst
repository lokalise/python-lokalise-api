.. index:: Getting started

Getting started
===============

Installation and requirements
-----------------------------

This plugin requires `Python 3.6 <http://www.python.org/>`_ or above
and `PIP <https://pypi.org/project/pip/>`_.

Install it by running:

.. code-block:: bash

  pip install python-lokalise-api

Initializing the client
-----------------------

In order to perform API requests, you `require a special token <https://app.lokalise.com/api2docs/curl/#resource-authentication>`_
that can be obtained in your personal Lokalise profile (*API tokens* section).

After you've obtained the token, import the plugin and initialize the client:

.. code-block:: python

  import lokalise
  client = lokalise.Client('YOUR_API_TOKEN')

Now use the ``client`` variable to perform API requests!
You may also check the :ref:`customizing-client` section to learn how to set timeouts.

Initializing the client with OAuth 2 token
------------------------------------------

You can also send API requests with `OAuth 2 tokens <https://docs.lokalise.com/en/articles/5574713-oauth-2>`_. To achieve that, you have to
instantiate a proper class:

.. code-block:: python

  import lokalise
  client = lokalise.OAuthClient('YOUR_OAUTH_API_TOKEN')

This class accepts the same options as a regular ``Client``ю

Objects and models
------------------

Individual objects retrieved from the API (projects, contributors, translation keys etc)
are represented as instances of
Python classes. They are called *models*. Each model responds to the methods
that are named after the API object attributes.

For example:

.. code-block:: python

  project = client.project('123.abc')
  project.name # => "Sample Project"
  project.description # => "This is a demo project."

  order = client.order(345, 5678)
  order.status # => "completed"
  order.provider_slug # => "gengo"

Many resources respond to common methods: ``project_id``,
``team_id``, ``user_id``, and ``branch``:

.. code-block:: python

  contributor = client.contributor('project.123.id', 456)
  contributor.project_id # => 'project.123.id'

  language = client.language('project.123.id', 21045)
  language.branch # => 'master'

You may also fetch raw data returned by the API:

.. code-block:: python

  project = client.project('123.abc')
  project.raw_data

.. _collections-pagination:

Collections of resources and pagination
---------------------------------------

Retrieving, creating, or updating multiple objects will return a *collection* of objects
(with individual objects represented as models).

.. code-block:: python

  projects = client.projects() # projects collection

To get access to the actual data, use ``items``:

.. code-block:: python

  print(projects.items)
  first_project = projects.items[0]
  first_project.name
  first_project.description

Bulk fetches support `pagination <https://app.lokalise.com/api2docs/curl/#resource-pagination>`_.
There are two common options available:

* ``"limit"`` (defaults to ``100``, maximum is ``5000``) - number of records to display per page.
* ``"page"`` (defaults to ``1``) - page to fetch.

For example:

.. code-block:: python

  client.projects({"limit": 2, "page": 3}) # 2 projects per page, get the 3rd page
  client.contributors('project.123', {"limit": 5}) # 5 contributors per page, get the 1st page

Collections has the following attributes (some of the attributes may be absent depending on the endpoint):

* ``current_page`` - the number of the current page.
* ``total_count`` - total number of records available.
* ``page_count`` - total number of pages available.
* ``limit`` - number of records per page.
* ``project_id`` - ID of the project that the collection belongs to.
* ``user_id`` - ID of the user the collection belongs to.
* ``team_id`` - ID of the team the collection belongs to.
* ``branch`` - project branch that the collection was fetched from.
* ``errors`` - errors that occured during the request processing. Usually this attribute is empty or absent, but it may contain a list of error messages in certain cases. For example, suppose you are creating multiple project languages, and one of the languages is incorrect. All languages with proper attributes will be created and returned as collection. ``errors`` will contain a list of errors explaining that one of the languages has incorrect attributes.

Collections respond to the following methods:

* ``is_last_page()``
* ``is_first_page()``
* ``has_next_page()``
* ``has_prev_page()``

For example:

.. code-block:: python

  projects = client.projects({"limit": 2, "page": 3})
  projects.is_last_page() # => True, this is the last page
  projects.has_next_page() # => False, no more pages available
  projects.has_prev_page() # => True, there is a previous page available

Branching
---------

If you are using `project branching feature <https://docs.lokalise.com/en/articles/3391861-project-branching>`_,
simply add a branch name separated by semicolon to your project ID in any endpoint to access the branch.
For example, in order to access the ``new-feature`` branch for the project with an id of ``123abcdef.01``:

.. code-block:: python

  contributors = client.contributors('123abcdef.01:new-feature')
  contributors.branch # => "new-feature"
  contributors.project_id # => "123abcdef.01"
  contributors.items[0].contributor_id # => 12345
