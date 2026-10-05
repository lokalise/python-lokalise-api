"""
lokalise.oauth_client
~~~~~~~~~~~~~~~~~~~~~
This module contains API client that can be used with OAuth 2 tokens.
"""

from .client import Client


class OAuthClient(Client):
    """Client used to send API requests with OAuth 2 tokens.

    Usage:

        import lokalise
        client = lokalise.OAuthClient('oauth2_api_token')
        client.projects()
    """

    TOKEN_HEADER = "Authorization"

    def _prepare_token(self, token: str) -> str:
        return f"Bearer {token}"
