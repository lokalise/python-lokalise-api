Files endpoint
==============

`Files documentation <https://developers.lokalise.com/reference/list-all-files>`_

Fetch all files
---------------

.. py:function:: files(project_id, [params = None])

  :param str project_id: ID of the project to fetch files for.
  :param dict params: (optional) :ref:`pagination options <collections-pagination>`
  :return: Collection of files

Example:

.. code-block:: python

  files = client.files('123.abc', {"page": 2, "limit": 1})
  files.items[0].filename # => "%LANG_ISO%.yml"

Upload file
-----------

.. py:function:: upload_file(project_id, params)

  :param str project_id: ID of the project to upload file to
  :param dict params: Upload params
  :return: Queued process model

Please note that the file upload will be performed in the background, and this method will
return a :ref:`QueuedProcess <queued-process>`. The QueuedProcess, in turn, will
contain the process ID and its status (`queued`, `running`, `finished` etc).
You can periodically check the process status to determine whether the upload
has completed.

Example:

.. code-block:: python

  process = client.upload_file('123.abc', {
      "data": 'ZnI6DQogIHRlc3Q6IHRyYW5zbGF0aW9u',
      "filename": 'python_upload.yml',
      "lang_iso": 'ru_RU'
  })
  process.status # => "queued"
  # ...
  # Update process status after some time:
  process = client.queued_process('123.abc', process.process_id)
  process.status # => "finished"
  # Your file is uploaded!

Download files
--------------

.. py:function:: download_files(project_id, params)

  :param str project_id: ID of the project to download from
  :param dict params: Download params
  :return: Dictionary with project ID and a bundle URL

Example:

.. code-block:: python

  response = client.download_files('123.abc', {
      "format": "json",
      "original_filenames": True,
      "replace_breaks": False
  })
  response['bundle_url'] # => "https://s3-eu-west-1.amazonaws.com/path/to/bundle.zip"

Delete file
-----------

Please note that this endpoint does not support "software localization" projects.

.. py:function:: delete_file(project_id, file_id)

  :param str project_id: ID of the project
  :param file_id: ID of the file to delete
  :return: Dictionary with project ID and "file_deleted" set to True

Example:

.. code-block:: python

  response = client.delete_file("123.abc", 1234)
  response['file_deleted'] # => True