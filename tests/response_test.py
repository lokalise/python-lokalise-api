
"""
Tests for API response parsing and error handling.
"""

from unittest.mock import Mock, patch

import pytest

from lokalise.response import ApiResponse
from lokalise.response_utils import respond_with_error


def test_response_uses_raw_body_when_json_is_invalid():
    response = Mock()
    response.json.side_effect = ValueError
    response.text = "not json"
    response.headers = {}
    response.status_code = 200

    with patch("lokalise.response.raise_on_error") as raise_on_error:
        result = ApiResponse(response)

    assert result["_raw_body"] == "not json"
    assert result.status_code == 200
    raise_on_error.assert_called_once_with(
        response,
        {"_raw_body": "not json"},
    )


def test_response_preserves_headers():
    response = Mock()
    response.json.return_value = {"projects": []}
    response.headers = {
        "X-Pagination-Page": "2",
        "X-Pagination-Page-Count": "5",
    }
    response.status_code = 200

    with patch("lokalise.response.raise_on_error"):
        result = ApiResponse(response)

    assert result["projects"] == []
    assert result.headers["x-pagination-page"] == "2"
    assert result.headers["X-PAGINATION-PAGE-COUNT"] == "5"
    assert "_pagination" not in result


def test_response_preserves_vantage_meta():
    response = Mock()
    response.json.return_value = {
        "data": [],
        "meta": {
            "count": 0,
            "cursor": None,
            "hasMore": False,
        },
    }
    response.headers = {}
    response.status_code = 200

    with patch("lokalise.response.raise_on_error"):
        result = ApiResponse(response)

    assert result["meta"]["count"] == 0
    assert result["meta"]["cursor"] is None
    assert result["meta"]["hasMore"] is False
    assert "_pagination" not in result


def test_response_too_big():
    response = Mock()
    response.json.return_value = {"bundle_url": "example.zip"}
    response.headers = {"X-Response-Too-Big": "true"}
    response.status_code = 200

    with patch("lokalise.response.raise_on_error"):
        result = ApiResponse(response)

    assert result.response_too_big is True
    assert "_response_too_big" not in result


def test_response_rejects_non_object_json():
    response = Mock()
    response.json.return_value = ["unexpected", "array"]
    response.text = '["unexpected", "array"]'
    response.headers = {}
    response.status_code = 200

    with patch("lokalise.response.raise_on_error"):
        with pytest.raises(
            TypeError,
            match="Expected API response JSON to be an object",
        ):
            ApiResponse(response)


def test_respond_with_error_uses_raw_body_when_present():
    """Check that _raw_body is used when present."""
    with patch(
        "lokalise.response_utils.errors.error_from_http"
    ) as error_from_http:
        error_from_http.side_effect = RuntimeError("boom")

        with pytest.raises(RuntimeError, match="boom"):
            respond_with_error({"_raw_body": "raw error text"}, 400)

        error_from_http.assert_called_once_with(
            400,
            message=None,
            headers=None,
            body_text="raw error text",
        )
