"""
Tests for the JWT endpoint.
"""

import pytest


PROJECT_ID = "2273827860c1e2473eb195.11207948"


@pytest.mark.vcr
def test_jwt(client):
    """Tests fetching of JWT
    """
    resp = client.jwt(PROJECT_ID)
    assert "eyJ0eXAiOiJKV1" in resp.jwt
