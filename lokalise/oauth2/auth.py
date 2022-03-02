"""
lokalise.oauth2.auth
~~~~~~~~~~~~~~~~~~~~
This module contains OAuth 2 flow client definition.
"""

import urllib.parse
from typing import Optional, Union, Dict, List
from .request import post, BASE_URL


class Auth:
    """OAuth 2 flow client used to request tokens.

    Usage:

        import lokalise
        client = lokalise.Auth('client id', 'client secret')
        url = client.auth()
        client.token('secret code')
        client.refresh('refresh token')
    """

    def __init__(self, client_id: str, client_secret: str):
        """Instantiate a new client.

        :param str token: Your Lokalise client ID.
        :param str token: Your Lokalise client secret.
        """
        self.client_id = client_id
        self.client_secret = client_secret

    def auth(self,
             scope: Union[List, str],
             redirect_uri: Optional[str] = None,
             state: Optional[str] = None) -> str:
        """Generate a new auth URL. Users have to visit it and explicitly approve the requested permissions

        :param scope: Requested scopes
        :type scope: list or str
        :param str redirect_uri: Optional redirect URI
        :param str redirect_uri: Optional state to protect from CSRF attacks
        :rtype str:
        """
        if isinstance(scope, List):
            scope = ' '.join(scope)

        params = {
            "client_id": self.client_id,
            "scope": scope
        }
        if state:
            params["state"] = state

        if redirect_uri:
            params["redirect_uri"] = redirect_uri

        return self.__build_uri(params)

    def token(self, code: str) -> Dict:
        """Requests a new OAuth 2 token by sending a HTTP POST request.

        :param code: Code obtained with the `auth` method
        """
        params = {
            "code": code,
            "grant_type": 'authorization_code'
        }
        params = {**self.__base_params(), **params}
        return post('token', params)

    def refresh(self, refresh_token: str) -> Dict:
        """Refreshes OAuth 2 token by sending a HTTP POST request.

        :param refresh_token: Refresh token obtained with the `token` method
        """
        params = {
            "refresh_token": refresh_token,
            "grant_type": 'refresh_token'
        }
        params = {**self.__base_params(), **params}
        return post('token', params)

    def __base_params(self) -> Dict:
        return {
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }

    def __build_uri(self, params: Dict) -> str:
        return BASE_URL + "auth?" + urllib.parse.urlencode(params)
