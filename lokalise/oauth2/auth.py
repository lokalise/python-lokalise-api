
"""
lokalise.oauth2.auth
~~~~~~~~~~~~~~~~~~~~
OAuth 2.0 client for generating auth URLs and exchanging/refreshing tokens.
"""

from collections.abc import Sequence
from urllib.parse import urlencode

from lokalise.request_utils import join_url
from lokalise.response import ApiResponse

from .request import BASE_URL, post


class Auth:
    """OAuth 2.0 flow client.

    Usage:

        import lokalise

        client = lokalise.Auth("client id", "client secret")
        url = client.auth(
            scope=["read_projects", "write_keys"],
            redirect_uri="https://app.example.com/callback",
            state="csrf123",
        )
        token = client.token("auth_code_from_callback")
        refreshed = client.refresh(token["refresh_token"])
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Create a new OAuth 2.0 client.

        Args:
            client_id: Lokalise OAuth client ID.
            client_secret: Lokalise OAuth client secret.
        """
        if not client_id:
            raise ValueError("client_id must be a non-empty string")
        if not client_secret:
            raise ValueError("client_secret must be a non-empty string")

        self.client_id = client_id
        self.client_secret = client_secret

    def auth(
        self,
        scope: Sequence[str] | str,
        redirect_uri: str | None = None,
        state: str | None = None,
    ) -> str:
        """Generate an authorization URL for the OAuth 2.0 flow."""
        scope_str = " ".join(scope) if not isinstance(scope, str) else scope

        if not scope_str.strip():
            raise ValueError("scope must not be empty")

        params = {
            "client_id": self.client_id,
            "scope": scope_str,
        }

        if state:
            params["state"] = state

        if redirect_uri:
            params["redirect_uri"] = redirect_uri

        return f"{join_url(BASE_URL, 'auth')}?{urlencode(params)}"

    def token(self, code: str) -> ApiResponse:
        """Exchange an authorization code for access and refresh tokens."""
        if not code:
            raise ValueError("code must be a non-empty string")

        params = {
            "grant_type": "authorization_code",
            "code": code,
            **self._base_params(),
        }

        return ApiResponse(post("token", params))

    def refresh(self, refresh_token: str) -> ApiResponse:
        """Refresh an access token using a refresh token."""
        if not refresh_token:
            raise ValueError("refresh_token must be a non-empty string")

        params = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            **self._base_params(),
        }

        return ApiResponse(post("token", params))

    def _base_params(self) -> dict[str, str]:
        """Return the OAuth client credentials."""
        return {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
