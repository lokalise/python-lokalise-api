"""
Tests for the Orders endpoint.
"""

import pytest


TEAM_ID = 176692
ORDER_ID = "20200122FTR"
PROJECT_ID = "454087345e09f3e7e7eae3.57891254"
SECOND_PROJECT_ID = "803826145ba90b42d5d860.46800099"


@pytest.mark.vcr
def test_orders(client):
    """Tests fetching of all orders
    """
    orders = client.orders(TEAM_ID)
    assert orders.items[0].order_id == "201903198B2"


@pytest.mark.vcr
def test_orders_pagination(client):
    """Tests fetching of all orders with pagination
    """
    orders = client.orders(TEAM_ID, {"page": 3, "limit": 2})
    assert orders.items[0].order_id == ORDER_ID
    assert orders.current_page == 3
    assert orders.total_count == 6
    assert orders.page_count == 3
    assert orders.limit == 2

    assert orders.is_last_page()
    assert not orders.is_first_page()
    assert not orders.has_next_page()
    assert orders.has_prev_page()


@pytest.mark.vcr
def test_order(client):
    """Tests fetching of an order
    """
    order = client.order(TEAM_ID, ORDER_ID)
    assert order.order_id == ORDER_ID
    assert order.project_id == "124505395e2074d880f724.35422706"
    assert not order.branch
    assert order.card_id == 2185
    assert order.status == "completed"
    assert order.created_at == "2020-01-22 12:04:15 (Etc/UTC)"
    assert order.created_at_timestamp == 1579694655
    assert order.created_by == 20181
    assert order.created_by_email == "bodrovis@protonmail.com"
    assert order.source_language_iso == "en"
    assert order.target_language_isos == ["ru_RU"]
    assert 35400063 in order.keys
    assert order.source_words['ru_RU'] == 3
    assert order.provider_slug == "gengo"
    assert order.translation_style == "friendly"
    assert order.translation_tier == 1
    assert order.translation_tier_name == "Professional translator"
    assert order.briefing == "test"
    assert order.total == 0.21
    assert order.payment_method is None


@pytest.mark.vcr
def test_create_order(client):
    """Tests creation of an order
    """
    order = client.create_order(TEAM_ID, {
        "project_id": PROJECT_ID,
        "card_id": 2185,
        "briefing": "nothing special",
        "source_language_iso": "en",
        "target_language_isos": ["ru_RU"],
        "keys": [34089721],
        "provider_slug": "gengo",
        "translation_tier": 1
    })
    assert order.project_id == PROJECT_ID
    assert order.card_id == 2185
    assert order.status == "in progress"
    assert order.provider_slug == "gengo"
    assert order.briefing == "nothing special"
    assert order.total == 0.14


@pytest.mark.vcr
def test_create_order_dry_run(client):
    """Tests creation of an order with a dry run option
    """
    order = client.create_order(TEAM_ID, {
        "project_id": SECOND_PROJECT_ID,
        "card_id": 2185,
        "briefing": "DRY RUN",
        "source_language_iso": "en",
        "target_language_isos": ["ru_RU"],
        "keys": [74189435],
        "provider_slug": "gengo",
        "translation_tier": 1,
        "dry_run": True
    })
    assert not order.order_id
    assert order.project_id == SECOND_PROJECT_ID
    assert order.branch == 'master'
    assert order.status == "draft"
    assert order.dry_run
