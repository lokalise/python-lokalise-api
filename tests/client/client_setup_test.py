"""
Tests for the Client class
"""

from typing import Any, cast

import lokalise
import pytest


def test_client_arguments():
    """Checks that client can receive token, timeout values, and enable_compression"""
    client = lokalise.Client("123abc", connect_timeout=5, read_timeout=3, enable_compression=True)
    assert client.token == "123abc"
    assert client.connect_timeout == 5
    assert client.read_timeout == 3
    assert client.enable_compression
    assert client.token_header == "X-Api-Token"


@pytest.mark.vcr
def test_client_timeout(client: lokalise.Client) -> None:
    """Checks that timeout value is used properly"""
    client.connect_timeout = 7
    projects = client.projects()
    assert projects.items[0].project_id == "2273827860c1e2473eb195.11207948"


@pytest.mark.vcr
def test_client_compression(client: lokalise.Client) -> None:
    """Checks that compression value is used properly"""
    client.enable_compression = True
    keys = client.keys(
        "803826145ba90b42d5d860.46800099", {"include_translations": "1", "page": 1, "limit": 5000}
    )
    assert keys.project_id == "803826145ba90b42d5d860.46800099"


@pytest.mark.vcr
def test_client_no_compression(client: lokalise.Client) -> None:
    """Checks that compression can be disabled"""
    client.enable_compression = False
    keys = client.keys(
        "803826145ba90b42d5d860.46800099", {"include_translations": "1", "page": 1, "limit": 5000}
    )
    assert keys.project_id == "803826145ba90b42d5d860.46800099"


@pytest.mark.vcr
def test_reset_client():
    """Checks that the client can be reset"""
    client = lokalise.Client("123abc", connect_timeout=5, read_timeout=3, enable_compression=True)
    assert client.connect_timeout == 5
    assert client.enable_compression

    # Run an API request so that an endpoint is lazily-loaded
    with pytest.raises(lokalise.errors.BadRequest):
        client.projects()

    client.reset_client()

    assert client.token == ""
    assert client.connect_timeout is None
    assert client.read_timeout is None
    assert not client.enable_compression

    # Now make sure that lazily-loaded endpoint was reset as well
    endpoint_attrs = [a for a in vars(client) if a.endswith("_endpoint")]
    for attr in endpoint_attrs:
        assert getattr(client, attr) is None


def make_client() -> lokalise.Client:
    return lokalise.Client("valid-token")


def test_token_setter_rejects_empty() -> None:
    client = make_client()
    with pytest.raises(ValueError, match="token must be a non-empty string"):
        client.token = ""


def test_token_setter_accepts_non_empty() -> None:
    client = make_client()
    client.token = "123abc"
    assert client.token == "123abc"


# ---------- connect_timeout ----------


@pytest.mark.parametrize("value", [-1, -0.1])
def test_connect_timeout_rejects_negative(value: int | float) -> None:
    client = make_client()
    with pytest.raises(ValueError, match="connect_timeout must be a non-negative number or None"):
        client.connect_timeout = value


@pytest.mark.parametrize("value", [None, 0, 0.0, 3, 2.5])
def test_connect_timeout_allows_non_negative_or_none(value: int | float) -> None:
    client = make_client()
    client.connect_timeout = value
    assert client.connect_timeout == value


# ---------- read_timeout ----------


@pytest.mark.parametrize("value", [-1, -0.1])
def test_read_timeout_rejects_negative(value: int | float) -> None:
    client = make_client()
    with pytest.raises(ValueError, match="read_timeout must be a non-negative number or None"):
        client.read_timeout = value  # type: ignore[assignment]


@pytest.mark.parametrize("value", [None, 0, 0.0, 3, 2.5])
def test_read_timeout_allows_non_negative_or_none(value: int | float | None) -> None:
    client = make_client()
    client.read_timeout = value
    assert client.read_timeout == value


# ---------- enable_compression ----------


@pytest.mark.parametrize(
    "inp, expected",
    [
        (None, False),
        (False, False),
        (True, True),
    ],
)
def test_enable_compression_bool_inputs(inp: bool | None, expected: bool) -> None:
    client = make_client()
    client.enable_compression = inp
    assert client.enable_compression is expected


@pytest.mark.parametrize(
    "inp, expected",
    [
        (0, False),
        (1, True),
        ("yes", True),
        ("", False),
    ],
)
def test_enable_compression_coerces_truthy_falsy(inp: object, expected: bool) -> None:
    client = make_client()
    client.enable_compression = cast(Any, inp)
    assert client.enable_compression is expected


# ---------- api_host ----------


@pytest.mark.parametrize(
    ("inp", "expected"),
    [
        (None, None),
        ("", None),
        ("   ", None),
        ("\n\t", None),
        ("api.example.com", "api.example.com"),
        ("  api.example.com  ", "  api.example.com  "),
    ],
)
def test_api_host_assignment_rules(inp: str | None, expected: str | None) -> None:
    client = make_client()
    client.api_host = inp
    assert client.api_host == expected


def test_reset_client_allows_reloading_endpoints(client: lokalise.Client) -> None:
    ep1 = client.get_endpoint("projects")
    assert ep1 is not None

    client.reset_client()

    ep2 = client.get_endpoint("projects")
    assert ep2 is not None
    assert ep2 is not ep1


def test_get_endpoint_populates_when_attr_is_none(client: lokalise.Client) -> None:
    setattr(client, "__projects_endpoint", None)
    ep = client.get_endpoint("projects")
    assert ep is not None
