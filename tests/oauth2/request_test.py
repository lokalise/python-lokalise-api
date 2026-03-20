"""
Tests for the request methods
"""

from unittest.mock import Mock, patch

from lokalise.oauth2.request import respond_with


def test_respond_with_uses_raw_body_when_json_is_invalid():
    response = Mock()
    response.json.side_effect = ValueError
    response.text = "not json"
    response.headers = {}

    with patch("lokalise.oauth2.request.raise_on_error"):
        result = respond_with(response)

    assert result["_raw_body"] == "not json"
