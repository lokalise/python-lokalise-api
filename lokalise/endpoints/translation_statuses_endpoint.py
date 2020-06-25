"""
lokalise.endpoints.translation_statuses_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing translation statuses endpoint.
"""
from typing import Union, Dict
from .base_endpoint import BaseEndpoint
from .. import request


class TranslationStatusesEndpoint(BaseEndpoint):
    """Describes translation statuses endpoint.
    """
    PATH = "projects/$parent_id/custom_translation_statuses/$resource_id"

    def colors(self, **ids: Union[str, int]) -> Dict:
        """Fetches available RGB colors that can be assigned to
        translation statuses.

        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids).strip('/')
        return request.get(self.client, path + '/colors')
