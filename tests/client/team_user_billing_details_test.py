"""
Tests for the TeamUserBillingDetails endpoint.
"""

import pytest
from lokalise.client import Client

TEAM_ID = 176692


@pytest.mark.vcr
def test_team_user_billing_details(client: Client) -> None:
    """Tests fetching of billing details for the team user"""
    details = client.team_user_billing_details(TEAM_ID)

    assert details.billing_email == "hello@example.com"
    assert details.country_code == "LV"
    assert details.zip == "LV-6543"
    assert details.state_code == ""
    assert details.address1 == "Sample line 1"
    assert details.address2 == "Sample line 2"
    assert details.city == "Riga"
    assert details.phone == "+371123456"
    assert details.company == "Self-employed"
    assert details.vatnumber == "123"


@pytest.mark.vcr
def test_create_team_user_billing_details(client: Client) -> None:
    """Tests creation of billing details for the team user"""
    details = client.create_team_user_billing_details(
        TEAM_ID, {"billing_email": "hello@example.com", "country_code": "LV", "zip": "LV-1234"}
    )
    assert details.zip == "LV-1234"
    assert details.country_code == "LV"


@pytest.mark.vcr
def test_update_team_user_billing_details(client: Client) -> None:
    """Tests updating of billing details for the team user"""
    details = client.update_team_user_billing_details(
        TEAM_ID,
        {
            "billing_email": "hello@example.com",
            "country_code": "LV",
            "zip": "LV-6543",
            "address1": "Sample line 1",
            "address2": "Sample line 2",
            "city": "Riga",
            "phone": "+371123456",
            "company": "Self-employed",
            "vatnumber": "123",
        },
    )
    assert details.zip == "LV-6543"
    assert details.company == "Self-employed"
