import os
from typing import Any
from urllib.parse import parse_qs, urlparse

import pytest
from lokalise import Auth
from lokalise.errors import BadRequest


def _query(url: str) -> dict[str, list[str]]:
    return parse_qs(urlparse(url).query, keep_blank_values=True)


def test_auth_builds_url_with_sequence_scope(auth_client: Auth) -> None:
    url = auth_client.auth(["read_projects", "write_team_groups"], "http://example.com", "123abc")
    q = _query(url)
    assert q["scope"] == ["read_projects write_team_groups"]
    assert q["state"] == ["123abc"]
    assert q["redirect_uri"] == ["http://example.com"]


def test_auth_builds_url_with_single_scope(auth_client: Auth) -> None:
    url = auth_client.auth("read_projects")
    q = _query(url)
    assert q["scope"] == ["read_projects"]
    assert "state" not in q
    assert "redirect_uri" not in q


@pytest.mark.vcr
def test_token(auth_client: Auth) -> None:
    code = os.getenv("OAUTH2_CODE") or "DUMMY_CODE"
    token: dict[str, Any] = auth_client.token(code)
    assert token["access_token"] == "stubbed token"
    assert token["refresh_token"] == "stubbed refresh"
    assert token["expires_in"] == 3600
    assert token["token_type"] == "Bearer"


@pytest.mark.vcr
def test_token_error(auth_client: Auth) -> None:
    with pytest.raises(BadRequest) as excinfo:
        auth_client.token("fake")
    exc = excinfo.value
    assert str(exc).startswith("400 POST https://app.lokalise.com/oauth2/token failed")
    assert exc.status_code == 400
    assert exc.parsed and exc.parsed.reason


@pytest.mark.vcr
def test_refresh(auth_client: Auth) -> None:
    refresh_token = os.getenv("OAUTH2_REFRESH_TOKEN") or "DUMMY_OAUTH2_REFRESH_TOKEN"
    token: dict[str, Any] = auth_client.refresh(refresh_token)
    assert token["access_token"] == "refreshed token"
    assert token["scope"] == "write_team_groups read_projects"
    assert token["expires_in"] == 3600
    assert token["token_type"] == "Bearer"
