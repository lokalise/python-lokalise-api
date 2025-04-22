Glossary terms endpoint
=======================

`Glossary terms documentation <https://developers.lokalise.com/reference/list-glossary-terms>`_

Fetch all glossary terms
------------------------

.. py:function:: glossary_terms(project_id, [params=None])

  :param str project_id: ID of the project
  :param dict params: Request parameters
  :return: Collection of glossary terms

This endpoint uses cursor-based pagination.

Example:

.. code-block:: python

  glossary_terms = client.glossary_terms(PROJECT_ID, {
    "limit": 2,
    "cursor": "12345"
  })

  glossary_term = glossary_terms.items[0]
  glossary_term.term # => "router"
  glossary_terms.next_cursor # => "5489103"


Fetch a glossary term
---------------------

.. py:function:: glossary_term(project_id, glossary_term_id)

  :param str project_id: ID of the project
  :param glossary_term_id: ID of the term to fetch
  :return: Glossary term model

Example:

.. code-block:: python

  glossary_term = client.glossary_term(PROJECT_ID, GLOSSARY_TERM_ID)

  glossary_term.term # => "router"
  glossary_term.description # => "A network device"
  glossary_term.translatable # => True


Create glossary terms
---------------------

.. py:function:: create_glossary_terms(project_id, params)

  :param str project_id: ID of the project
  :param params: Glossary terms parameters
  :type params: list or dict
  :return: Glossary terms collection

Example:

.. code-block:: python

  glossary_terms = client.create_glossary_terms(PROJECT_ID, [
      {
          "term": "python",
          "description": "sample desc",
          "caseSensitive": False,
          "forbidden": False,
          "translatable": True,
          "tags": ["term1"]
      },
      {
          "term": "code editor",
          "description": "",
          "caseSensitive": False,
          "forbidden": False,
          "translatable": True,
          "translations": [{
              "langId": 674,
              "translation": "éditeur de code",
              "description": (
                  "Logiciel permettant d’écrire, modifier "
                  "et organiser du code informatique."
              )
          }],
          "tags": ["term2"]
      },
  ])

  term0 = glossary_terms.items[0]
  term1 = glossary_terms.items[1]
  
  term0.term # => "python"
  term1.tags # => ["term2"]


Update glossary terms
---------------------

.. py:function:: update_glossary_terms(project_id, params)

  :param str project_id: ID of the project
  :param dict params: Glossary terms parameters
  :return: Glossary terms collection

Example:

.. code-block:: python

  updated_terms = client.update_glossary_terms(PROJECT_ID, [
      {
          "id": GLOSSARY_TERM_ID,
          "description": "updated description",
          "caseSensitive": False
      }
  ])

  term = updated_terms.items[0]

  term.description # => "updated description"
  term.caseSensitive # => False


Delete glossary terms
---------------------

.. py:function:: delete_glossary_terms(project_id, glossary_terms_ids)

  :param str project_id: ID of the project
  :type glossary_terms_id: int or str
  :param list glossary_terms_ids: List of the term IDs to delete
  :return: Delete response
  :rtype dict:

Example:

.. code-block:: python

  response = client.delete_glossary_terms(PROJECT_ID, [5489360, 5489361])

  deleted_info = response['data']['deleted']

  deleted_info['count'] # => 2
  deleted_info['ids'][0] # => 5489360