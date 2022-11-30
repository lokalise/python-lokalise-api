"""
lokalise.base_client
~~~~~~~~~~~~~~~~~~~~
This module contains base API client definition.
"""
from typing import Optional, Union


class BaseClient:
    """Base client used to send API requests.
    """

    def __init__(self,
                 token: str,
                 connect_timeout: Optional[Union[int, float]] = None,
                 read_timeout: Optional[Union[int, float]] = None,
                 enable_compression: Optional[bool] = False) -> None:
        """Instantiate a new Lokalise API client.

        :param str token: Your Lokalise API token.
        :param connect_timeout: (optional) Server connection timeout
        (the value is in seconds). By default, the client will wait indefinitely.
        :type connect_timeout: int or float
        :param read_timeout: (optional) Server read timeout
        (the value is in seconds). By default, the client will wait indefinitely.
        :type read_timeout: int or float
        :param enable_compression: (optional) Whether to enable gzip compression.
        By default it's off.
        :type enable_compression: bool
        """
        self.token = token
        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout
        self.enable_compression = enable_compression
        self.token_header = 'X-Api-Token'
