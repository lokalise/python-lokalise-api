Permission templates endpoint
=============================

`Permission templates documentation <https://developers.lokalise.com/reference/list-all-permission-templates>`_

Fetch all permission templates
------------------------------

.. py:function:: permission_templates(team_id)

  :param team_id: ID of the team
  :type team_id: str or int

Example:

.. code-block:: python

  templates = client.permission_templates(12345)
  
  template.id # => 1
  template.role # => "Manager"
  template.permissions # => ['branches_main_modify', ...]
  template.description # => 'Manage project settings ...'
  template.tag # => 'Full access'
  template.tagColor # => 'green'
  template.tagInfo # => ''
  template.doesEnableAllReadOnlyLanguages # => true