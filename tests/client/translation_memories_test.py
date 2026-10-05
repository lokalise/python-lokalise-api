"""
Tests for the Translation memories endpoint.
"""

import pytest
from lokalise.client import Client

PROJECT_ID = "7565202469c53c30428ce0.33693563"


@pytest.mark.vcr
def test_translation_memories(client: Client) -> None:
    """Tests fetching of all translation memories"""
    tms = client.translation_memories(PROJECT_ID)
    assert tms.project_id == PROJECT_ID

    first_tm = tms.items[0]
    assert first_tm.name == "Lokalise Translation Memory"

    second_tm = tms.items[1]
    assert second_tm.id == 2592
