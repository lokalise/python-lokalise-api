"""
Tests for the Translation providers endpoint.
"""

import pytest


TEAM_ID = 176692
PROVIDER_ID = 4


@pytest.mark.vcr
def test_translation_providers(client):
    """Tests fetching of all translation providers
    """
    providers = client.translation_providers(TEAM_ID)
    assert providers.items[0].name == "Gengo"


@pytest.mark.vcr
def test_translation_providers_pagination(client):
    """Tests fetching of all translation providers with pagination
    """
    providers = client.translation_providers(TEAM_ID, {
        "page": 2,
        "limit": 1
    })
    assert providers.items[0].name == "Lokalise"
    assert providers.current_page == 2
    assert providers.total_count == 2
    assert providers.page_count == 2
    assert providers.limit == 1

    assert providers.is_last_page()
    assert not providers.is_first_page()
    assert not providers.has_next_page()
    assert providers.has_prev_page()


@pytest.mark.vcr
def test_translation_provider(client):
    """Tests fetching of a translation provider
    """
    provider = client.translation_provider(TEAM_ID, PROVIDER_ID)
    assert provider.provider_id == PROVIDER_ID
    assert provider.name == "Lokalise"
    assert provider.slug == "lokalise"
    assert provider.price_pair_min == "10.00"
    assert "lokalise" in provider.website_url
    assert "professional translations" in provider.description
    assert provider.tiers[0]["title"] == \
        "Translation only by a native professional linguist"
    assert provider.pairs[0]['from_lang_iso'] == "ru"
