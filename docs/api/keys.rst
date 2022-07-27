Keys endpoint
=============

`Keys documentation <https://developers.lokalise.com/reference/list-all-keys>`_

Fetch all keys
--------------

.. py:function:: keys(project_id, [params=None])

  :param str project_id: ID of the project
  :param dict params: Request parameters
  :return: Collection of keys

Please note that this endpoint should not be treated as a content delivery network
for your language files. It means that you should not perform a new request to this endpoint
with every website/app visitor. Instead, fetch this endpoint from time to time,
store the result locally and serve your visitors with static files/your database content.
Alternatively, you may use our Amazon S3/Google CloudStorage integrations in
automatically upload your language files to a bucket of your choice.

Example:

.. code-block:: python

  client.keys('123.abc', {
      "page": 2,
      "limit": 3,
      "disable_references": "1",
      "filter_archived": "exclude"
  })

Create keys
-----------

.. py:function:: create_keys(project_id, params)

  :param str project_id: ID of the project
  :param params: Keys parameters
  :type params: list or dict
  :return: Keys collection

Example:

.. code-block:: python

  client.create_keys('123.abc', [
      {
          "key_name": "python_1",
          "platforms": ["ios", "android"],
          "description": "Created by Python"
      },
      {
          "key_name": "python_2",
          "platforms": ["web"],
          "translations": [
              {
                  "language_iso": "en",
                  "translation": "Hi from Python"
              }
          ]
      }
  ])

Fetch a key
-----------

.. py:function:: key(project_id, key_id, [params=None])

  :param str project_id: ID of the project
  :param key_id: ID of the key to fetch
  :param dict params: Request parameters
  :return: Key model

Example:

.. code-block:: python

  key = client.key('123.abc', 3456, {"disable_references": "1"})
  key.key_id # => 3456
  key.key_name['ios'] # => "manual_setup"

Update a key
------------

.. py:function:: update_key(project_id, key_id, [params = None])

  :param str project_id: ID of the project
  :param key_id: ID of the key to update
  :param dict params: Request parameters
  :return: Key model

Example:

.. code-block:: python

  key = client.update_key('123.abc', 3456, {
      "description": "Updated by Python",
      "tags": ["python"]
  })
  key.description # => "Updated by Python"

Bulk key update
---------------

.. py:function:: update_keys(project_id, params)

  :param str project_id: ID of the project
  :param dict params: Key parameters
  :return: Key collection

Example:

.. code-block:: python

  keys = client.update_keys('123.abc', [
      {
          "key_id": 48855757,
          "description": "Bulk updated",
          "tags": ["bulk-python"]
      },
      {
          "key_id": 48855758,
          "translations": [
              {
                  "language_iso": "en",
                  "translation": "Updated Python translation"
              }
          ]
      }
  ])
  keys.items[0].description # => "Bulk updated"

Delete a key
------------

.. py:function:: delete_key(project_id, key_id)

  :param str project_id: ID of the project
  :param key_id: ID of the key to delete
  :type key_id: int or str
  :return: Dictionary with project ID and "key_removed" set to True
  :rtype dict:

Example:

.. code-block:: python

  client.delete_key('123.abc', 48850)

Delete multiple keys
--------------------

.. py:function:: delete_keys(project_id, key_ids)

  :param str project_id: ID of the project
  :type key_id: int or str
  :param list key_ids: List of the key identifiers to delete
  :return: Dictionary with project ID and "keys_removed" set to True
  :rtype dict:

Example:

.. code-block:: python

  client.delete_keys('123.abc', [34567, 78913])
