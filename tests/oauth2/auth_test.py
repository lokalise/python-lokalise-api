import os
from typing import Any
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse

import pytest
from lokalise import Auth
from lokalise.errors import BadRequest


def _query(url: str) -> dict[str, list[str]]:
    return parse_qs(urlparse(url).query, keep_blank_values=True)


def test_auth_builds_url_with_sequence_scope(auth_client: Auth) -> None:
    url = auth_client.auth(
        ["read_projects", "write_team_groups"],
        "http://example.com",
        "123abc",
    )

    parsed = urlparse(url)
    q = parse_qs(parsed.query, keep_blank_values=True)

    assert parsed.scheme == "https"
    assert parsed.netloc == "app.lokalise.com"
    assert parsed.path == "/oauth2/auth"

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
    message = str(exc)

    assert message.startswith("400 code: Code must be 40 characters long")
    assert "POST https://app.lokalise.com/oauth2/token failed" in message
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


@pytest.mark.parametrize(
    ("client_id", "client_secret", "message"),
    [
        ("", "secret", "client_id must be a non-empty string"),
        ("client-id", "", "client_secret must be a non-empty string"),
    ],
)
def test_auth_rejects_empty_credentials(
    client_id: str,
    client_secret: str,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        Auth(client_id, client_secret)


@pytest.mark.parametrize(
    "scope",
    [
        "",
        "   ",
        [],
    ],
)
def test_auth_rejects_empty_scope(
    auth_client: Auth,
    scope: str | list[str],
) -> None:
    with pytest.raises(ValueError, match="scope must not be empty"):
        auth_client.auth(scope)


def test_refresh_rejects_empty_token(auth_client: Auth) -> None:
    with pytest.raises(
        ValueError,
        match="refresh_token must be a non-empty string",
    ):
        auth_client.refresh("")


def test_token_sends_authorization_code_params(
    auth_client: Auth,
) -> None:
    response = {"access_token": "token"}

    with patch(
        "lokalise.oauth2.auth.post",
        return_value=response,
    ) as post_mock:
        result = auth_client.token("auth-code")

    assert result == response
    post_mock.assert_called_once_with(
        "token",
        {
            "grant_type": "authorization_code",
            "code": "auth-code",
            "client_id": auth_client.client_id,
            "client_secret": auth_client.client_secret,
        },
    )


def test_token_rejects_empty_code(auth_client: Auth) -> None:
    with pytest.raises(
        ValueError,
        match="code must be a non-empty string",
    ):
        auth_client.token("")


def test_refresh_sends_refresh_token_params(
    auth_client: Auth,
) -> None:
    response = {"access_token": "token"}

    with patch(
        "lokalise.oauth2.auth.post",
        return_value=response,
    ) as post_mock:
        result = auth_client.refresh("refresh-token")

    assert result == response
    post_mock.assert_called_once_with(
        "token",
        {
            "grant_type": "refresh_token",
            "refresh_token": "refresh-token",
            "client_id": auth_client.client_id,
            "client_secret": auth_client.client_secret,
        },
    )
