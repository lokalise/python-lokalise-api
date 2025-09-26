"""
lokalise.client_methods.branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for branches.
"""

from typing import Any

from lokalise.collections.branches import BranchesCollection
from lokalise.models.branch import BranchModel

from .endpoint_provider import EndpointProviderMixin


class BranchMethods(EndpointProviderMixin):
    """Branch client methods."""

    def branches(
        self, project_id: str, params: dict[str, int | str] | None = None
    ) -> BranchesCollection:
        """Fetches all branches for the given project.

        :param str project_id: ID of the project to fetch branches for.
        :param dict params: (optional) Pagination params
        :return: Collection of branches
        """
        raw_branches = self.get_endpoint("branches").all(parent_id=project_id, params=params)
        return BranchesCollection(raw_branches)

    def branch(self, project_id: str, branch_id: str | int) -> BranchModel:
        """Fetches a single branch.

        :param str project_id: ID of the project
        :param branch_id: ID of the branch to fetch
        :type branch_id: int or str
        :return: Branch model
        """
        raw_branch = self.get_endpoint("branches").find(parent_id=project_id, resource_id=branch_id)
        return BranchModel(raw_branch)

    def create_branch(self, project_id: str, params: dict[str, str]) -> BranchModel:
        """Creates a new branch inside the project

        :param str project_id: ID of the project
        :param dict params: Branch parameters
        :return: Branch model
        """
        raw_branch = self.get_endpoint("branches").create(params=params, parent_id=project_id)

        return BranchModel(raw_branch)

    def update_branch(
        self, project_id: str, branch_id: str | int, params: dict[str, str]
    ) -> BranchModel:
        """Updates a branch.

        :param str project_id: ID of the project
        :param branch_id: ID of the branch to update
        :type branch_id: int or str
        :param dict params: Update parameters
        :return: Branch model
        """
        raw_branch = self.get_endpoint("branches").update(
            params=params, parent_id=project_id, resource_id=branch_id
        )
        return BranchModel(raw_branch)

    def delete_branch(self, project_id: str, branch_id: str | int) -> dict[str, Any]:
        """Deletes a branch.

        :param str project_id: ID of the project
        :param branch_id: ID of the branch to delete
        :type branch_id: int or str
        :return: Dictionary with project ID and "branch_deleted" set to True
        :rtype dict:
        """
        response = self.get_endpoint("branches").delete(parent_id=project_id, resource_id=branch_id)
        return response

    def merge_branch(
        self,
        project_id: str,
        branch_id: str | int,
        params: dict[str, str | int] | None = None,
    ) -> dict[str, Any]:
        """Merges a branch.

        :param str project_id: ID of the project
        :param branch_id: ID of the source branch
        :type branch_id: int or str
        :param dict params: Merge parameters
        :return: Dictionary with project ID, "branch_merged" set to True, and branches info
        :rtype dict:
        """
        response = self.get_endpoint("branches").merge(
            params=params, parent_id=project_id, resource_id=branch_id
        )
        response["branch"] = BranchModel(response["branch"])
        response["target_branch"] = BranchModel(response["target_branch"])
        return response
