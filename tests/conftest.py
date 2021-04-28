"""
Contains fixture functions for the tests.
"""


import os
import pytest
from dotenv import load_dotenv, find_dotenv
import lokalise

load_dotenv(find_dotenv())


@pytest.fixture(scope='module')
def vcr_config():
    """Configuration for the VCR module
    """
    return {
        "filter_headers": [('x-api-token', 'FILTERED')],
        "decode_compressed_response": True
    }


@pytest.fixture(scope='module')
def vcr_cassette_dir(request):
    """Sets the path to save cassettes to.
    """
    return os.path.join(f"tests/cassettes/{request.module.__name__}")


@pytest.fixture(scope='module')
def screenshot_data():
    """Loads base64-encoded screenshot data.
    """
    try:
        with open(os.path.join("tests/fixtures/screenshot_base64.txt"), 'r') as file:
            data = file.read()
    except FileNotFoundError:
        return ''
    else:
        file.close()
        return data


@pytest.fixture(scope='module')
def client():
    """Creates a sample client object using the token from the ENV.
    """
    return lokalise.Client(os.getenv("LOKALISE_API_TOKEN"))
