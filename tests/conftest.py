import os
import pytest
from dotenv import load_dotenv, find_dotenv
import lokalise

load_dotenv(find_dotenv())


@pytest.fixture(scope='module')
def vcr_config():
    return {
        "filter_headers": [('x-api-token', 'FILTERED')],
        "decode_compressed_response": True
    }


@pytest.fixture(scope='module')
def vcr_cassette_dir(request):
    return os.path.join(f"tests/cassettes/{request.module.__name__}")


@pytest.fixture(scope='module')
def client():
    return lokalise.Client(os.getenv("LOKALISE_API_TOKEN"))
