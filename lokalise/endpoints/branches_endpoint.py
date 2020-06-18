"""
lokalise.endpoints.branches_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing branches endpoint.
"""
from typing import Dict, List, Union, Optional
from .base_endpoint import BaseEndpoint


class BranchesEndpoint(BaseEndpoint):
    """Describes project branches endpoint.
    """
    PATH = "projects/{project_id}/branches/{resource_id}"
