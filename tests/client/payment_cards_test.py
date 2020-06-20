"""
Tests for the PaymentCards endpoint.
"""

import pytest


CARD_ID = 2185
NEW_CARD_ID = 3514

@pytest.mark.vcr
def test_payment_cards(client):
    """Tests fetching of all payment cards
    """
    cards = client.payment_cards({"page": 2, "limit": 1})
    assert cards.user_id == 20181
    assert cards.items[0].card_id == CARD_ID
    assert cards.current_page == 2
    assert cards.total_count == 2
    assert cards.page_count == 2
    assert cards.limit == 1

    assert cards.is_last_page()
    assert not cards.is_first_page()
    assert not cards.has_next_page()
    assert cards.has_prev_page()


@pytest.mark.vcr
def test_payment_card(client):
    """Tests fetching of a payment card
    """
    card = client.payment_card(CARD_ID)
    assert card.user_id == 20181
    assert card.card_id == CARD_ID
    assert card.last4 == "8148"
    assert card.brand == "MasterCard"
    assert card.created_at == "2019-06-19 15:51:54 (Etc/UTC)"
    assert card.created_at_timestamp == 1560959514


@pytest.mark.vcr
def test_create_payment_card(client):
    """Tests creation of a payment card
    """
    card = client.create_payment_card({
        "number": "4242424242420391",
        "cvc": 123,
        "exp_month": 9,
        "exp_year": 2025
    })
    assert card.last4 == "0391"
    assert card.brand == "Visa"


@pytest.mark.vcr
def test_delete_payment_card(client):
    """Tests deletion of a payment card
    """
    resp = client.delete_payment_card(NEW_CARD_ID)
    assert resp['card_id'] == NEW_CARD_ID
    assert resp['card_deleted']
