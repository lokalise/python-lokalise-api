from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
import pytest
import lokalise

@pytest.mark.vcr
def test_it():
    client = lokalise.Client(os.getenv("LOKALISE_API_TOKEN"))
    p = client.projects()
    print(p)
    assert True == True
