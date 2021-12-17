"""
Tests for the Segments endpoint.
"""

import pytest


PROJECT_ID = "39066161618d4ecb9fdc12.00274309"
LANG_ISO = "en"
KEY_ID = 134490810
SEGMENT_NUMBER = 1


@pytest.mark.vcr
def test_segments(client):
    """Tests fetching of all segments
    """
    segments = client.segments(
        PROJECT_ID, KEY_ID, LANG_ISO, {
            "disable_references": '1'})
    assert segments.project_id == PROJECT_ID
    assert segments.items[0].language_iso == LANG_ISO
    assert segments.items[1].modified_by == 20181


@pytest.mark.vcr
def test_segment(client):
    """Tests fetching of a segment
    """
    segment = client.segment(
        PROJECT_ID, KEY_ID, LANG_ISO, SEGMENT_NUMBER, {
            "disable_references": '1'})

    assert segment.segment_number == SEGMENT_NUMBER
    assert segment.language_iso == LANG_ISO
    assert segment.modified_at == "2021-12-16 17:00:53 (Etc/UTC)"
    assert segment.modified_at_timestamp == 1639674053
    assert segment.modified_by == 20181
    assert segment.modified_by_email == "bodrovis@protonmail.com"
    assert segment.value == "Hello!"
    assert segment.is_fuzzy
    assert not segment.is_reviewed
    assert segment.reviewed_by == 0
    assert segment.words == 1
    assert segment.custom_translation_statuses == []


@pytest.mark.vcr
def test_update_segment(client):
    """Tests updating of a segment
    """
    segment = client.update_segment(
        PROJECT_ID, KEY_ID, LANG_ISO, 2, {
            "value": "Hello from Python!",
            "is_reviewed": True
        })

    assert segment.segment_number == 2
    assert segment.value == "Hello from Python!"
    assert segment.custom_translation_statuses[0]["title"] == "context"
