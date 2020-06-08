from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import pytest
import lokalise
import os

@pytest.fixture(scope='module')
def vcr_config():
    return {
        "filter_headers": [('x-api-token', 'FILTERED')],
        "decode_compressed_response": True
    }

@pytest.fixture(scope='module')
def vcr_cassette_dir(request):
    return os.path.join('tests/cassettes')

@pytest.fixture(scope='module')
def client():
    return lokalise.Client(os.getenv("LOKALISE_API_TOKEN"))
