"""
Tests for the PermissionTemplates endpoint.
"""

import pytest
from lokalise.client import Client

TEAM_ID = 176692


@pytest.mark.vcr
def test_permission_templates(client: Client) -> None:
    """Tests fetching of all permission templates"""
    templates = client.permission_templates(TEAM_ID)

    template = templates.items[0]

    assert template.id == 1
    assert template.role == "Manager"
    assert "branches_main_modify" in template.permissions
    assert template.description == "Manage project settings, contributors and tasks"
    assert template.tag == "Full access"
    assert template.tagColor == "green"
    assert template.tagInfo is None
    assert template.doesEnableAllReadOnlyLanguages is True
