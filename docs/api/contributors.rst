Contributors endpoint
=====================

`Contributors documentation <https://app.lokalise.com/api2docs/curl/#resource-contributors>`_

Fetch all contributors
----------------------

.. py:function:: contributors(project_id, [params={}])

  :param str project_id: ID of the project to fetch contributors for.
  :param dict params: (optional) :ref:`pagination options <collections-pagination>`
  :return: Collection of contributors

Fetch a single contributor
--------------------------

.. py:function:: contributor(project_id, contributor_id)

  :param str project_id: ID of the project
  :param contributor_id: ID of the contributor to fetch
  :type contributor_id: int or str
  :return: Contributor model
