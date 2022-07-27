Segments endpoint
=================

`Segments documentation <https://developers.lokalise.com/reference/list-all-segments-for-key-language>`_

Fetch all segments
------------------

.. py:function:: segments(project_id, key_id, lang_iso, [params = None])

  :param str project_id: ID of the project
  :param str key_id: ID of the key
  :type key_id: int or str
  :param str lang_iso: Language ISO code
  :param dict params: (optional) Additional params
  :return: Collection of segments

Example:

.. code-block:: python

  client.segments("123.abc", 4567, "en-US", {"disable_references": '1'})

Fetch a segment
---------------

.. py:function:: segment(project_id, key_id, lang_iso, segment_number, [params = None])

  :param str project_id: ID of the project
  :param str key_id: ID of the key
  :type key_id: int or str
  :param str lang_iso: Language ISO code
  :param str segment_number: Number of the segment
  :type segment_number: int or str
  :param dict params: (optional) Additional params
  :return: Segment model

Example:

.. code-block:: python

  client.segment("123.abc", 4567, "en-US", 2, {"disable_references": '1'})

Update a segment
----------------

.. py:function:: update_segment(project_id, key_id, lang_iso, segment_number, params)

  :param str project_id: ID of the project
  :param str key_id: ID of the key
  :type key_id: int or str
  :param str lang_iso: Language ISO code
  :param str segment_number: Number of the segment
  :type segment_number: int or str
  :param dict params: Segment params
  :return: Segment model

Example:

.. code-block:: python

  client.update_segment("123.abc", 4567, "en-US", 2, {
      "value": "Hello from Python!",
      "is_reviewed": True
  })