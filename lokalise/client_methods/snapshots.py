"""
lokalise.client_methods.snapshots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for snapshots.
"""
from typing import Optional, Union, Dict
from lokalise.models.snapshot import SnapshotModel
from lokalise.models.project import ProjectModel
from lokalise.collections.snapshots import SnapshotsCollection
from .endpoint_provider import EndpointProviderMixin


class SnapshotMethods(EndpointProviderMixin):
    """Snapshot client methods.
    """

    def snapshots(self, project_id: str,
                  params: Optional[Dict] = None) -> SnapshotsCollection:
        """Fetches all snapshots for the given project.

        :param str project_id: ID of the project
        :param dict params: (optional) Pagination params
        :return: Collection of snapshots
        """
        raw_snapshots = self.get_endpoint("snapshots"). \
            all(params=params, parent_id=project_id)
        return SnapshotsCollection(raw_snapshots)

    def create_snapshot(self, project_id: str,
                        params: Optional[Dict[str, str]] = None
                        ) -> SnapshotModel:
        """Creates a snapshot of the given project.

        :param str project_id: ID of the project
        :param dict params: (optional) Request params
        :return: Snapshot model
        """
        raw_snapshot = self.get_endpoint("snapshots"). \
            create(params=params, parent_id=project_id)
        return SnapshotModel(raw_snapshot)

    def restore_snapshot(self,
                         project_id: str,
                         snapshot_id: Union[str, int]) -> ProjectModel:
        """Restores a snapshot of the given project by producing a new project.

        :param str project_id: ID of the project
        :param queued_process_id: ID of the snapshot to restore
        :type snapshot_id: int or str
        :return: Snapshot model
        """
        new_project = self.get_endpoint("snapshots"). \
            create(parent_id=project_id, resource_id=snapshot_id)
        return ProjectModel(new_project)

    def delete_snapshot(self, project_id: str,
                        snapshot_id: Union[str, int]) -> Dict:
        """Deletes a project snapshot.

        :param str project_id: ID of the project
        :param snapshot_id: ID of the snapshot to delete
        :return: Dictionary with project ID and "snapshot_deleted" set to True
        :rtype dict:
        """
        response = self.get_endpoint("snapshots"). \
            delete(parent_id=project_id, resource_id=snapshot_id)
        return response
