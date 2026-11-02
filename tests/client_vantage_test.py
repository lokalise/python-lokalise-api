
from unittest.mock import Mock, patch
from requests import Response

from lokalise import ClientVantage
from lokalise.request import get
from lokalise.response import ApiResponse


def test_vantage_client_defaults():
    client = ClientVantage("test-token")

    assert client.token == "test-token"
    assert client.token_header == "X-Api-Token"
    assert client.api_host == "https://api.lokalise.com/vantage/v1/"
    assert client.connect_timeout is None
    assert client.read_timeout is None
    assert client.enable_compression is False


def test_vantage_client_options():
    client = ClientVantage(
        "test-token",
        connect_timeout=5,
        read_timeout=10,
        enable_compression=True,
        api_host="https://example.com/custom/",
    )

    assert client.api_host == "https://example.com/custom/"
    assert client.connect_timeout == 5
    assert client.read_timeout == 10
    assert client.enable_compression is True


def test_vantage_client_request() -> None:
    client = ClientVantage("test-token")

    raw_response = Mock(spec=Response)
    raw_response.status_code = 200
    raw_response.headers = {}
    raw_response.json.return_value = {"data": []}

    with patch(
        "lokalise.request.requests.request",
        return_value=raw_response,
    ) as mocked_request:
        result = get(client, "projects/project-id/items")

    # The request layer must return the original HTTP response.
    assert result is raw_response
    raw_response.json.assert_not_called()

    mocked_request.assert_called_once()

    args, kwargs = mocked_request.call_args

    assert args == (
        "GET",
        "https://api.lokalise.com/vantage/v1/projects/project-id/items",
    )
    assert kwargs["headers"]["X-Api-Token"] == "test-token"
    assert kwargs["headers"]["Accept"] == "application/json"

    # Response parsing is handled separately.
    parsed = ApiResponse(result)

    assert parsed["data"] == []