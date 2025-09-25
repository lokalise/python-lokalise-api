"""
lokalise.models.team_user_billing_detail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing team users billing details model.
"""

from .base_model import BaseModel


class TeamUsersBillingDetailsModel(BaseModel):
    """Describes team users billing details model."""

    DATA_KEY = ""

    ATTRS = [
        "billing_email",
        "country_code",
        "zip",
        "state_code",
        "address1",
        "address2",
        "city",
        "phone",
        "company",
        "vatnumber",
    ]
