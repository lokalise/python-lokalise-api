Translation memories endpoint
=============================

`Translation memories documentation <https://developers.lokalise.com/reference/list-project-translation-memories>`_

Fetch all translation memories
------------------------------

.. py:function:: translation_memories(project_id)

  :param str project_id: ID of the project
  :return: Collection of translation memories

Example:

.. code-block:: python

  tms = client.translation_memories('123.abc')
  tms.items[0].name # => "Custom TM"
