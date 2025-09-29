"""
lokalise.client_methods.permission_templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for permission templates.
"""

from lokalise.collections.permission_templates import PermissionTemplatesCollection

from .endpoint_provider import EndpointProviderMixin


class PermissionTemplateMethods(EndpointProviderMixin):
    """Permission template client methods."""

    def permission_templates(self, team_id: int | str) -> PermissionTemplatesCollection:
        """Fetches all permission templates for the given team.

        :param team_id: ID of the team
        :type team_id: int or str
        :return: Collection of permission templates
        """
        raw_templates = self.get_endpoint("permission_templates").all(parent_id=team_id)
        return PermissionTemplatesCollection(raw_templates)
