import pytest

@pytest.fixture(scope='module')
def vcr_config():
    return {
        "filter_headers": [('x-api-token', 'FILTERED')],
        "decode_compressed_response": True
    }
