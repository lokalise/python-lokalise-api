"""
Tests for the request methods
"""

from unittest.mock import Mock, patch

from lokalise.oauth2.request import respond_with


def test_respond_with_uses_raw_body_when_json_is_invalid() -> None:
    response = Mock()
    response.json.side_effect = ValueError
    response.text = "not json"
    response.headers = {}

    with patch("lokalise.oauth2.request.raise_on_error") as raise_mock:
        result = respond_with(response)

    assert result == {"_raw_body": "not json"}
    raise_mock.assert_called_once_with(
        response,
        {"_raw_body": "not json"},
    )


def test_respond_with_returns_json_object() -> None:
    response = Mock()
    response.json.return_value = {
        "access_token": "token",
        "token_type": "Bearer",
    }
    response.text = ""
    response.headers = {}

    with patch("lokalise.oauth2.request.raise_on_error") as raise_mock:
        result = respond_with(response)

    expected = {
        "access_token": "token",
        "token_type": "Bearer",
    }

    assert result == expected
    raise_mock.assert_called_once_with(response, expected)


def test_respond_with_uses_raw_body_when_json_is_not_object() -> None:
    response = Mock()
    response.json.return_value = ["unexpected", "payload"]
    response.text = '["unexpected", "payload"]'
    response.headers = {}

    with patch("lokalise.oauth2.request.raise_on_error") as raise_mock:
        result = respond_with(response)

    expected = {
        "_raw_body": '["unexpected", "payload"]',
    }

    assert result == expected
    raise_mock.assert_called_once_with(response, expected)
