"""
lokalise.client_methods.screenshots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for screenshots.
"""

from typing import Any, Optional, Union

from lokalise.collections.screenshots import ScreenshotsCollection
from lokalise.models.screenshot import ScreenshotModel

from .endpoint_provider import EndpointProviderMixin


class ScreenshotMethods(EndpointProviderMixin):
    """Screenshot client methods."""

    def screenshots(
        self, project_id: str, params: Optional[dict[str, str | int]] = None
    ) -> ScreenshotsCollection:
        """Fetches all screenshots for the given project.

        :param str project_id: ID of the project
        :param dict params: (optional) Pagination params
        :return: Collection of screenshots
        """
        raw_screenshots = self.get_endpoint("screenshots").all(params=params, parent_id=project_id)
        return ScreenshotsCollection(raw_screenshots)

    def screenshot(self, project_id: str, screenshot_id: Union[str, int]) -> ScreenshotModel:
        """Fetches a screenshot.

        :param str project_id: ID of the project
        :param screenshot_id: ID of the screenshot to fetch
        :type screenshot_id: int or str
        :return: Screenshot model
        """
        screenshot = self.get_endpoint("screenshots").find(
            parent_id=project_id, resource_id=screenshot_id
        )
        return ScreenshotModel(screenshot)

    def create_screenshots(
        self, project_id: str, params: Union[list[dict[str, Any]], dict[str, Any]]
    ) -> ScreenshotsCollection:
        """Creates one or more screenshots in the given project.

        :param str project_id: ID of the project
        :param params: Screenshots parameters
        :type params: dict or list
        :return: Collection of screenshots
        """
        raw_screenshots = self.get_endpoint("screenshots").create(
            params=params, wrapper_attr="screenshots", parent_id=project_id
        )
        return ScreenshotsCollection(raw_screenshots)

    def update_screenshot(
        self,
        project_id: str,
        screenshot_id: Union[str, int],
        params: Optional[dict[str, Any]] = None,
    ) -> ScreenshotModel:
        """Updates a screenshot.

        :param str project_id: ID of the project
        :param screenshot_id: ID of the screenshot to update
        :type screenshot_id: int or str
        :param dict params: Screenshots parameters
        :return: Screenshot model
        """
        screenshot = self.get_endpoint("screenshots").update(
            params=params, parent_id=project_id, resource_id=screenshot_id
        )
        return ScreenshotModel(screenshot)

    def delete_screenshot(self, project_id: str, screenshot_id: Union[str, int]) -> dict[str, Any]:
        """Deletes a screenshot.

        :param str project_id: ID of the project
        :param screenshot_id: ID of the screenshot to delete
        :type screenshot_id: int or str
        :return: Dictionary with the project ID and "screenshot_deleted": True
        """
        response = self.get_endpoint("screenshots").delete(
            parent_id=project_id, resource_id=screenshot_id
        )
        return response
