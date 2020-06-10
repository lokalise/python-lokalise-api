Projects endpoint
=================

`Projects documentation <https://app.lokalise.com/api2docs/curl/#resource-projects>`_

Fetch all projects
------------------

.. py:function:: projects([params={}])

  :param dict params: (optional) :ref:`pagination options <collections-pagination>`
  :return: Collection of projects

Fetch a single project
----------------------

.. py:function:: project(project_id)

  :param str project_id: ID of the project to fetch
  :return: Project model
