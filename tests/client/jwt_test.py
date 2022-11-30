"""
Tests for the JWT endpoint.
"""

import pytest


@pytest.mark.vcr
def test_jwt(client):
    """Tests fetching of JWT
    """
    resp = client.jwt()
    assert "eyJ0eXAiOiJK" in resp.jwt
