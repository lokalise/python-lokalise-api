"""
Tests for the Auth class.
"""

import os
import pytest
from lokalise.errors import BadRequest


@pytest.mark.vcr
def test_auth(auth_client):
    """Tests auth method
    """
    url = auth_client.auth(
        ["read_projects", "write_team_groups"], "http://example.com", '123abc')

    assert r"read_projects+write_team_groups" in url
    assert r"&state=123abc" in url
    assert r"c&redirect_uri=http%3A%2F%2Fexample.com" in url


@pytest.mark.vcr
def test_auth_single_scope(auth_client):
    """Tests auth method with a single scope
    """
    url = auth_client.auth("read_projects")

    assert r"read_projects" in url


@pytest.mark.vcr
def test_token(auth_client):
    """Tests token method
    """
    token = auth_client.token(os.getenv("OAUTH2_CODE"))
    assert token['access_token'] == 'stubbed token'
    assert token['refresh_token'] == 'stubbed refresh'
    assert token['expires_in'] == 3600
    assert token['token_type'] == 'Bearer'


@pytest.mark.vcr
def test_token_error(auth_client):
    """Tests token method exception handling
    """
    with pytest.raises(BadRequest) as excinfo:
        auth_client.token("fake")
    assert excinfo.value.args[0] == 'invalid_request'
    assert excinfo.value.args[1] == 400


@pytest.mark.vcr
def test_refresh(auth_client):
    """Tests refresh method
    """
    token = auth_client.refresh(os.getenv("OAUTH2_REFRESH_TOKEN"))
    assert token['access_token'] == 'refreshed token'
    assert token['scope'] == "write_team_groups read_projects"
    assert token['expires_in'] == 3600
    assert token['token_type'] == 'Bearer'
