Comments endpoint
=================

`Comments documentation <https://app.lokalise.com/api2docs/curl/#resource-comments>`_

Fetch all project comments
--------------------------

.. py:function:: project_comments(project_id, [params = None])

  :param str project_id: ID of the project to fetch comments for.
  :param dict params: (optional) :ref:`pagination options <collections-pagination>`
  :return: Collection of comments

Example:

.. code-block:: python

  client.project_comments('123.abc', {"page": 2, "limit": 1})

Fetch all key comments
----------------------

.. py:function:: key_comments(project_id, key_id, [params = None])

  :param str project_id: ID of the project
  :param key_id: ID of key to fetch comments for
  :type key_id: int or str
  :param dict params: (optional) :ref:`pagination options <collections-pagination>`
  :return: Collection of comments

Example:

.. code-block:: python

  client.key_comments('123.abc', 3456, {"limit": 1, "page": 2})

Fetch key comment
-----------------

.. py:function:: key_comment(project_id, key_id, comment_id)

  :param str project_id: ID of the project
  :param key_id: ID of key to fetch comments for
  :type key_id: int or str
  :param comment_id: Comment identifier to fetch
  :type comment_id: int or str
  :return: Comment model

Example:

.. code-block:: python

  comment = client.key_comment('123.abc', 3456, 1234)
  comment.key_id # => 3456
  comment.added_by_email # => "test@example.com"

Create key comments
-------------------

.. py:function:: create_key_comments(project_id, key_id, params)

  :param str project_id: ID of the project
  :param key_id: ID of key to create comments for
  :type key_id: int or str
  :param params: Comment parameters
  :type params: list or dict
  :return: Collection of comments

Example:

.. code-block:: python

  client.create_key_comments('123.abc', 3456, [
      {
          "comment": "Python comment 1"
      }, {
          "comment": "Python comment 2"
      }
  ])

Delete key comment
------------------

.. py:function:: delete_key_comment(project_id, key_id, comment_id)

  :param str project_id: ID of the project
  :param key_id: ID of key to delete comment for.
  :type key_id: int or str
  :param comment_id: Comment to delete
  :type comment_id: int or str
  :return: Dictionary with project ID and "comment_deleted" set to True

Example:

.. code-block:: python

  client.delete_key_comment('123.abc', 3456, 9838)
