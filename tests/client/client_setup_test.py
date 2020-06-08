import pytest
import lokalise

def test_client_arguments():
    client = lokalise.Client("123abc", connect_timeout = 5, read_timeout = 3)
    assert client.token == "123abc"
    assert client.connect_timeout == 5
    assert client.read_timeout == 3

def test_reset_client():
    client = lokalise.Client("123abc", connect_timeout = 5, read_timeout = 3)
    assert client.token == "123abc"

    client.reset_client()

    assert client.token == None
    assert client.connect_timeout == None
    assert client.read_timeout == None
    endpoint_attrs = [a for a in vars(client) if a.endswith('_endpoint')]
    for attr in endpoint_attrs:
        assert getattr(client, attr) == None
