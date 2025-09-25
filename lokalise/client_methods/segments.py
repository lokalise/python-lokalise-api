"""
lokalise.client_methods.segments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for segments.
"""

from typing import Any, Optional, Union

from lokalise.collections.segments import SegmentsCollection
from lokalise.models.segment import SegmentModel

from .endpoint_provider import EndpointProviderMixin


class SegmentMethods(EndpointProviderMixin):
    """Segment client methods."""

    def segments(
        self,
        project_id: str,
        key_id: Union[str, int],
        lang_iso: str,
        params: Optional[dict[str, Any]] = None,
    ) -> SegmentsCollection:
        """Fetches all segments for the given key and language inside a project.

        :param str project_id: ID of the project
        :param str key_id: ID of the key
        :type key_id: int or str
        :param str lang_iso: Language ISO code
        :param dict params: (optional) Additional params
        :return: Collection of segments
        """
        raw_segments = self.get_endpoint("segments").all(
            params=params, parent_id=project_id, resource_id=key_id, subresource_id=lang_iso
        )
        return SegmentsCollection(raw_segments)

    def segment(
        self,
        project_id: str,
        key_id: Union[str, int],
        lang_iso: str,
        segment_number: Union[str, int],
        params: Optional[dict[str, Any]] = None,
    ) -> SegmentModel:
        """Fetches a segment for the given key and language inside a project.

        :param str project_id: ID of the project
        :param str key_id: ID of the key
        :type key_id: int or str
        :param str lang_iso: Language ISO code
        :param str segment_number: Number of the segment
        :type segment_number: int or str
        :param dict params: (optional) Additional params
        :return: Segment model
        """
        raw_segment = self.get_endpoint("segments").find(
            params=params,
            parent_id=project_id,
            resource_id=key_id,
            subresource_id=f"{lang_iso}/{segment_number}",
        )
        return SegmentModel(raw_segment)

    def update_segment(
        self,
        project_id: str,
        key_id: Union[str, int],
        lang_iso: str,
        segment_number: Union[str, int],
        params: dict[str, Any],
    ) -> SegmentModel:
        """Updates a segment.

        :param str project_id: ID of the project
        :param str key_id: ID of the key
        :type key_id: int or str
        :param str lang_iso: Language ISO code
        :param str segment_number: Number of the segment
        :type segment_number: int or str
        :param dict params: New segment attributes
        :return: Segment model
        """
        raw_segment = self.get_endpoint("segments").update(
            params=params,
            parent_id=project_id,
            resource_id=key_id,
            subresource_id=f"{lang_iso}/{segment_number}",
        )
        return SegmentModel(raw_segment)
