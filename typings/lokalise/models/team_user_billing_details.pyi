from lokalise.models.base_model import BaseModel

class TeamUsersBillingDetailsModel(BaseModel):
    billing_email: str
    country_code: str
    zip: str
    state_code: str
    address1: str
    address2: str
    city: str
    phone: str
    company: str
    vatnumber: str
