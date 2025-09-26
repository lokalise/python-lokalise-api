"""
Tests for custom exceptions
"""

import lokalise
import pytest

PROJECT_ID = "454087345e09f3e7e7eae3.57891254"


@pytest.mark.vcr
def test_not_found(client: lokalise.Client) -> None:
    """Checks that the NotFound exception is raised when
    the resource cannot be found
    """
    with pytest.raises(lokalise.errors.NotFound) as excinfo:
        client.project("123/invalid/")

    exc = excinfo.value
    assert exc.status_code == 404


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

    assert excinfo.value.status_code == 400


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
