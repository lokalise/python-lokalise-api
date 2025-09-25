"""
lokalise.oauth2.auth
~~~~~~~~~~~~~~~~~~~~
OAuth 2.0 client for generating auth URLs and exchanging/refreshing tokens.
"""

import urllib.parse
from typing import Any, Sequence

from .request import BASE_URL, post


class Auth:
    """OAuth 2.0 flow client.

    Usage:

        import lokalise
        client = lokalise.Auth("client id", "client secret")
        url = client.auth(scope=["read_projects", "write_keys"], redirect_uri="https://app.example.com/callback", state="csrf123")
        token = client.token("auth_code_from_callback")
        refreshed = client.refresh(token["refresh_token"])
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Instantiate a new OAuth 2 client.

        :param client_id: Lokalise OAuth client ID
        :param client_secret: Lokalise OAuth client secret
        """
        self.client_id = client_id
        self.client_secret = client_secret

    def auth(
        self,
        scope: Sequence[str] | str,
        redirect_uri: str | None = None,
        state: str | None = None,
    ) -> str:
        """Generate the authorization URL users should visit to approve access.

        :param scope: Requested scopes (either a sequence of scope strings or a single space-delimited string)
        :param redirect_uri: Optional redirect URI registered with your OAuth client
        :param state: Optional state to protect from CSRF (will be returned back)
        :return: Absolute URL to redirect the user to
        """
        scope_str = " ".join(scope) if not isinstance(scope, str) else scope

        params: dict[str, str] = {
            "client_id": self.client_id,
            "scope": scope_str,
        }
        if state:
            params["state"] = state
        if redirect_uri:
            params["redirect_uri"] = redirect_uri

        return self.__build_uri(params)

    def token(self, code: str) -> dict[str, Any]:
        """Exchange an authorization code for an access/refresh token.

        :param code: Authorization code received from the `auth()` redirect
        :return: Parsed JSON payload with tokens and metadata
        """
        params: dict[str, str] = {
            "grant_type": "authorization_code",
            "code": code,
            **self.__base_params(),
        }
        return post("token", params)

    def refresh(self, refresh_token: str) -> dict[str, Any]:
        """Refresh an access token using a refresh token.

        :param refresh_token: Refresh token obtained from a previous `token()` call
        :return: Parsed JSON payload with new tokens and metadata
        """
        params: dict[str, str] = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            **self.__base_params(),
        }
        return post("token", params)

    # --- internals ---------------------------------------------------------

    def __base_params(self) -> dict[str, str]:
        return {"client_id": self.client_id, "client_secret": self.client_secret}

    def __build_uri(self, params: dict[str, str]) -> str:
        base = BASE_URL.rstrip("/")
        query = urllib.parse.urlencode(params, doseq=True)
        return f"{base}/auth?{query}"
