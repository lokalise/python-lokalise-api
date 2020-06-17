"""
lokalise.endpoints.system_languages_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing system languages endpoint.
"""

from .base_endpoint import BaseEndpoint


class SystemLanguagesEndpoint(BaseEndpoint):
    """Describes system languages endpoint.
    """
    PATH = "system/languages"
