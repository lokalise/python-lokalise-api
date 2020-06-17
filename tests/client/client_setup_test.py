"""
Tests for the Client class
"""

import pytest
import lokalise


def test_client_arguments():
    """Checks that client can receive token and timeout values
    """
    client = lokalise.Client("123abc", connect_timeout=5, read_timeout=3)
    assert client.token == "123abc"
    assert client.connect_timeout == 5
    assert client.read_timeout == 3


@pytest.mark.vcr
def test_client_timeout(client):
    """Checks that timeout value is used properly
    """
    client.connect_timeout = 7
    projects = client.projects()
    assert projects.items[0].project_id == "638597985c913f818559f3.17106287"


@pytest.mark.vcr
def test_reset_client():
    """Checks that the client can be reset
    """
    client = lokalise.Client("123abc", connect_timeout=5, read_timeout=3)
    assert client.connect_timeout == 5

    # Run an API request so that an endpoint is lazily-loaded
    with pytest.raises(lokalise.errors.BadRequest):
        client.projects()

    client.reset_client()

    assert client.token is None
    assert client.connect_timeout is None
    assert client.read_timeout is None

    # Now make sure that lazily-loaded endpoint was reset as well
    endpoint_attrs = [a for a in vars(client) if a.endswith('_endpoint')]
    for attr in endpoint_attrs:
        assert getattr(client, attr) is None
