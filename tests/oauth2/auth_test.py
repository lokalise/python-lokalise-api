"""
Tests for the Auth class.
"""

import os

import pytest

from lokalise.errors import BadRequest
from lokalise import Auth


@pytest.mark.vcr
def test_auth(auth_client: Auth) -> None:
    """Tests auth method"""
    url = auth_client.auth(["read_projects", "write_team_groups"], "http://example.com", "123abc")

    assert r"read_projects+write_team_groups" in url
    assert r"&state=123abc" in url
    assert r"c&redirect_uri=http%3A%2F%2Fexample.com" in url


@pytest.mark.vcr
def test_auth_single_scope(auth_client: Auth) -> None:
    """Tests auth method with a single scope"""
    url = auth_client.auth("read_projects")

    assert r"read_projects" in url


@pytest.mark.vcr
def test_token(auth_client: Auth) -> None:
    """Tests token method"""
    code = os.getenv("OAUTH2_CODE") or "DUMMY_CODE"
    token = auth_client.token(code)
    assert token["access_token"] == "stubbed token"
    assert token["refresh_token"] == "stubbed refresh"
    assert token["expires_in"] == 3600
    assert token["token_type"] == "Bearer"


@pytest.mark.vcr
def test_token_error(auth_client: Auth) -> None:
    """Tests token method exception handling"""
    with pytest.raises(BadRequest) as excinfo:
        auth_client.token("fake")
    exc = excinfo.value
    assert str(exc).startswith("400 POST https://app.lokalise.com/oauth2/token failed")
    assert exc.status_code == 400
    assert exc.parsed and exc.parsed.reason


@pytest.mark.vcr
def test_refresh(auth_client: Auth) -> None:
    """Tests refresh method"""
    refresh_token = os.getenv("OAUTH2_REFRESH_TOKEN") or "DUMMY_OAUTH2_REFRESH_TOKEN"
    token = auth_client.refresh(refresh_token)
    assert token["access_token"] == "refreshed token"
    assert token["scope"] == "write_team_groups read_projects"
    assert token["expires_in"] == 3600
    assert token["token_type"] == "Bearer"
