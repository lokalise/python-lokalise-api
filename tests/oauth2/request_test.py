
"""
Tests for OAuth2 HTTP requests.
"""

import json
from unittest.mock import Mock, patch

from requests import Response

from lokalise.oauth2 import request as oauth_request


def test_post_uses_shared_transport() -> None:
    """Check that OAuth2 POST uses the shared HTTP transport."""
    raw_response = Mock(spec=Response)

    params = {
        "grant_type": "refresh_token",
        "refresh_token": "abc123",
    }

    with patch(
        "lokalise.request.requests.request",
        return_value=raw_response,
    ) as request_mock:
        result = oauth_request.post("token", params)

    assert result is raw_response
    raw_response.json.assert_not_called()

    request_mock.assert_called_once()

    args, kwargs = request_mock.call_args

    assert args == (
        "POST",
        "https://app.lokalise.com/oauth2/token",
    )

    assert json.loads(kwargs["data"]) == params

    headers = kwargs["headers"]

    assert headers["Accept"] == "application/json"
    assert headers["Content-Type"] == "application/json"
    assert "User-Agent" in headers

    assert "Authorization" not in headers
    assert "X-Api-Token" not in headers

    assert kwargs["timeout"] is None


def test_post_without_params() -> None:
    """Check that OAuth2 POST accepts requests without parameters."""
    raw_response = Mock(spec=Response)

    with patch(
        "lokalise.oauth2.request.send",
        return_value=raw_response,
    ) as send_mock:
        result = oauth_request.post("revoke")

    assert result is raw_response

    send_mock.assert_called_once_with(
        "POST",
        "https://app.lokalise.com/oauth2/revoke",
        params=None,
        headers={
            "Accept": "application/json",
            "User-Agent": oauth_request.base_headers()["User-Agent"],
            "Content-Type": "application/json",
        },
    )
