Team user billing details endpoint
==================================

`Team user billing details documentation <https://developers.lokalise.com/reference/retrieve-team-user-billing-details>`_

Fetch team user billing details
-------------------------------

.. py:function:: team_user_billing_details(team_id)

  :param str team_id: ID of the team
  :return: Team users billing details model

Example:

.. code-block:: python

  details = client.team_user_billing_details(1234)
  details.billing_email # => "hello@example.com"
  details.address1 # => "Sample line 1"

Create team user billing details
--------------------------------

.. py:function:: create_team_user_billing_details(team_id, params)

  :param str team_id: ID of the team
  :param dict params: Billing details parameters
  :return: Team users billing details model

Example:

.. code-block:: python

  details = client.create_team_user_billing_details(1234, {
      "billing_email": "hello@example.com",
      "country_code": "LV",
      "zip": "LV-1234"
  })
  details.zip # => "LV-1234"
  details.country_code # => "LV"

Update team user billing details
--------------------------------

.. py:function:: update_team_user_billing_details(team_id, params)

  :param str team_id: ID of the team
  :param dict params: Billing details parameters
  :return: Team users billing details model

Example:

.. code-block:: python

  details = client.update_team_user_billing_details(1234, {
      "city": "Riga",
      "phone": "+371123456",
      "company": "Self-employed",
      "vatnumber": "123"
  })
  details.city # => "Riga"
  details.company # => "Self-employed"