"""
Tests for the Client class
"""

import pytest
import lokalise


def test_client_arguments():
    """Checks that client can receive token, timeout values, and enable_compression
    """
    client = lokalise.Client(
        "123abc",
        connect_timeout=5,
        read_timeout=3,
        enable_compression=True)
    assert client.token == "123abc"
    assert client.connect_timeout == 5
    assert client.read_timeout == 3
    assert client.enable_compression


@pytest.mark.vcr
def test_client_timeout(client):
    """Checks that timeout value is used properly
    """
    client.connect_timeout = 7
    projects = client.projects()
    assert projects.items[0].project_id == "2273827860c1e2473eb195.11207948"


@pytest.mark.vcr
def test_client_compression(client):
    """Checks that compression value is used properly
    """
    client.enable_compression = True
    keys = client.keys(
        '803826145ba90b42d5d860.46800099', {
            "include_translations": "1", "page": 1, "limit": 5000})
    assert keys.project_id == "803826145ba90b42d5d860.46800099"


@pytest.mark.vcr
def test_client_no_compression(client):
    """Checks that compression can be disabled
    """
    client.enable_compression = False
    keys = client.keys(
        '803826145ba90b42d5d860.46800099', {
            "include_translations": "1", "page": 1, "limit": 5000})
    assert keys.project_id == "803826145ba90b42d5d860.46800099"


@pytest.mark.vcr
def test_reset_client():
    """Checks that the client can be reset
    """
    client = lokalise.Client(
        "123abc",
        connect_timeout=5,
        read_timeout=3,
        enable_compression=True)
    assert client.connect_timeout == 5
    assert client.enable_compression

    # Run an API request so that an endpoint is lazily-loaded
    with pytest.raises(lokalise.errors.BadRequest):
        client.projects()

    client.reset_client()

    assert client.token == ''
    assert client.connect_timeout is None
    assert client.read_timeout is None
    assert not client.enable_compression

    # Now make sure that lazily-loaded endpoint was reset as well
    endpoint_attrs = [a for a in vars(client) if a.endswith('_endpoint')]
    for attr in endpoint_attrs:
        assert getattr(client, attr) is None
