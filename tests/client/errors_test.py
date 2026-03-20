"""
Tests for custom exceptions
"""

import lokalise
import pytest
from lokalise.errors import (
    APIError,
    ClientHTTPError,
    NotFound,
    _as_int_maybe,  # pyright: ignore[reportPrivateUsage]
    _coalesce,  # pyright: ignore[reportPrivateUsage]
    _pick_details,  # pyright: ignore[reportPrivateUsage]
    error_from_http,
    parse_api_error,
)

PROJECT_ID = "454087345e09f3e7e7eae3.57891254"


@pytest.mark.vcr
def test_not_found(client: lokalise.Client) -> None:
    """Checks that the NotFound exception is raised when
    the resource cannot be found
    """
    with pytest.raises(lokalise.errors.NotFound) as excinfo:
        client.project("123/invalid/")

    exc = excinfo.value
    assert isinstance(exc, lokalise.errors.ClientHTTPError)
    assert exc.status_code == 404
    assert isinstance(exc.message, str)
    assert isinstance(exc.headers, dict)
    assert isinstance(exc.raw_text, str) or exc.raw_text is None
    assert exc.parsed is not None
    assert isinstance(exc.parsed, lokalise.errors.APIError)
    assert exc.parsed.status == 404
    assert isinstance(exc.parsed.message, str)
    assert isinstance(exc.parsed.reason, str)
    assert exc.parsed.code is None or isinstance(exc.parsed.code, (int, str))
    assert exc.parsed.details is None or isinstance(exc.parsed.details, dict)


@pytest.mark.vcr
def test_unknown_error(client: lokalise.Client) -> None:
    """Checks that the basic ClientError is raised for
    an unknown error code
    """
    with pytest.raises(lokalise.errors.ClientError) as excinfo:
        client.project("very/invalid/path")
    assert excinfo.value.args[1] == 407


@pytest.mark.vcr
def test_no_error_key(client: lokalise.Client) -> None:
    """Checks that the error gets handled even if the `error`
    key is not found in the response
    """
    with pytest.raises(lokalise.errors.ClientError) as excinfo:
        client.project("wrong/path")
    assert excinfo.value.args[1] == 404


@pytest.mark.vcr
def test_invalid_client():
    """Check that a BadRequest is raised when the client has
    invalid token
    """
    invalid_client = lokalise.Client("invalid")
    with pytest.raises(lokalise.errors.BadRequest) as excinfo:
        invalid_client.projects()

    exc = excinfo.value
    assert exc.status_code == 400
    assert isinstance(exc.message, str)
    assert isinstance(exc.headers, dict)
    assert isinstance(exc.raw_text, str)
    assert exc.parsed is not None
    assert exc.parsed.status == 400
    assert isinstance(exc.parsed.details, (dict, type(None)))


@pytest.mark.vcr
def test_errors(client: lokalise.Client) -> None:
    """Tests edge case when the response has "errors" key
    but the response is 200
    """
    resp = client.create_languages(
        PROJECT_ID, [{"lang_iso": "fr"}, {"lang_iso": "by", "custom_iso": "by_2"}]
    )
    assert (
        resp.errors[0]["message"] == "`lang_iso` parameter should be in a scope of system languages"
    )


def test_parse_api_error_non_json_body():
    """Checks non-JSON error body fallback"""
    err = parse_api_error("oops", 500)

    assert err.status == 500
    assert err.message == "Internal Server Error"
    assert err.reason == "non-json error body"
    assert err.raw == "oops"
    assert err.code is None
    assert err.details is None


def test_parse_api_error_empty_body():
    """Checks empty body fallback"""
    err = parse_api_error("", 404)

    assert err.status == 404
    assert err.message == "Not Found"
    assert err.reason == "empty body"
    assert err.raw == ""
    assert err.code is None
    assert err.details is None


def test_parse_api_error_invalid_json_body():
    """Checks invalid JSON body fallback"""
    err = parse_api_error('{"broken"', 400)

    assert err.status == 400
    assert err.message == "Bad Request"
    assert err.reason == "invalid json in error body"
    assert err.raw == '{"broken"'
    assert err.code is None
    assert err.details == {"unmarshal_error": "json decode failed"}


def test_parse_api_error_top_level_format():
    """Checks top-level API error format"""
    err = parse_api_error(
        '{"message":"Nope","statusCode":401,"error":"Unauthorized"}',
        401,
    )

    assert err.status == 401
    assert err.message == "Nope"
    assert err.reason == "Unauthorized"
    assert err.code == 401
    assert err.details == {
        "message": "Nope",
        "statusCode": 401,
        "error": "Unauthorized",
    }


def test_parse_api_error_nested_error_without_numeric_code():
    """Checks nested error format with fallback code and wrapped details"""
    err = parse_api_error(
        '{"error":{"message":"Bad stuff","code":"abc","details":"boom"}}',
        423,
    )

    assert err.status == 423
    assert err.message == "Bad stuff"
    assert err.reason == "nested error"
    assert err.code == 423
    assert err.details == {"details": "boom"}


def test_parse_api_error_top_level_error_code():
    """Checks alternate top-level format with errorCode"""
    err = parse_api_error(
        '{"message":"Slow down","errorCode":"429","details":["x"]}',
        429,
    )

    assert err.status == 429
    assert err.message == "Slow down"
    assert err.reason == "top-level"
    assert err.code == 429
    assert err.details == {"details": ["x"]}


def test_parse_api_error_fallback_unhandled_format():
    """Checks fallback for unhandled JSON error format"""
    err = parse_api_error('{"foo":"bar"}', 418)

    assert err.status == 418
    assert err.message == "HTTP 418 Error"
    assert err.reason == "unhandled error format"
    assert err.code is None
    assert err.details == {"foo": "bar"}


def test_error_from_http_returns_specific_http_error():
    """Checks that mapped status code returns specific exception type"""
    exc = error_from_http(
        404,
        headers={"x-test": "1"},
        body_text='{"message":"Missing","statusCode":404,"error":"Not Found"}',
    )

    assert isinstance(exc, NotFound)
    assert exc.status_code == 404
    assert exc.message == "Missing"
    assert exc.headers == {"x-test": "1"}
    assert exc.raw_text == '{"message":"Missing","statusCode":404,"error":"Not Found"}'
    assert exc.parsed is not None
    assert exc.parsed.reason == "Not Found"
    assert exc.parsed.code == 404


def test_error_from_http_returns_generic_http_error_for_unknown_status():
    """Checks that unknown status code returns generic ClientHTTPError"""
    exc = error_from_http(418, body_text="teapot")

    assert type(exc) is ClientHTTPError
    assert exc.status_code == 418
    assert exc.message == "HTTP 418 Error"
    assert exc.raw_text == "teapot"
    assert exc.parsed is not None
    assert exc.parsed.reason == "non-json error body"


def test_client_http_error_str_includes_reason_and_code():
    """Checks string representation of parsed HTTP error"""
    exc = ClientHTTPError(
        "Nope",
        400,
        parsed=APIError(
            status=400,
            message="Nope",
            reason="validation failed",
            raw="{}",
            code="E123",
            details=None,
        ),
    )

    assert str(exc) == "400 Nope | reason=validation failed | code='E123'"


def test_coalesce_returns_empty_string_when_all_values_are_empty():
    """Checks that _coalesce returns empty string when no truthy values are provided"""
    assert _coalesce(None, "", None) == ""


def test_as_int_maybe_returns_false_for_bool():
    """Checks that bool is not treated as int"""
    assert _as_int_maybe(True) == (0, False)


def test_as_int_maybe_converts_float_to_int():
    """Checks that float is converted to int"""
    assert _as_int_maybe(12.8) == (12, True)


def test_as_int_maybe_returns_false_when_int_conversion_fails():
    """Checks that failed int conversion returns (0, False)"""

    class WeirdStr(str):
        def strip(self, chars: str | None = None) -> "WeirdStr":
            return self

        def __int__(self) -> int:
            raise RuntimeError("boom")

    assert _as_int_maybe(WeirdStr("123")) == (0, False)


def test_pick_details_returns_details_dict_as_is():
    """Checks that _pick_details returns details when it is already a dict"""
    assert _pick_details({"details": {"field": "name"}}) == {"field": "name"}
