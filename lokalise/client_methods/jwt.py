"""
lokalise.client_methods.jwt
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for JWT.
"""
from typing import Optional, Dict, Any
from lokalise.models.jwt import JwtModel
from .endpoint_provider import EndpointProviderMixin


class JwtMethods(EndpointProviderMixin):
    """JWT client methods.
    """

    def jwt(
        self,
        project_id: str,
        params: Optional[Dict[str, Any]] = None
    ) -> JwtModel:
        """Creates OTA JWT.

        :return: JWT model
        """
        if params is None:
            params = {"service": "ota"}

        raw_jwt = self.get_endpoint("jwt").create(
            parent_id=project_id, params=params)
        return JwtModel(raw_jwt)
