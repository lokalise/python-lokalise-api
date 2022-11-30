"""
lokalise.models.jwt
~~~~~~~~~~~~~~~~~~~
Module containing JWT model.
"""

from .base_model import BaseModel


class JwtModel(BaseModel):
    """Describes JWT.
    """
    ATTRS = [
        'jwt'
    ]
