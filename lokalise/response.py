
"""
lokalise.response
~~~~~~~~~~~~~~~~~
HTTP response parsing and error handling.
"""

from typing import Any, cast

from requests import Response
from requests.structures import CaseInsensitiveDict

from .response_utils import raise_on_error


class ApiResponse(dict[str, Any]):
    """Parsed API response with HTTP metadata."""

    def __init__(self, response: Response) -> None:
        try:
            raw_data: object = response.json()
        except ValueError:
            raw_data = {"_raw_body": response.text}

        if not isinstance(raw_data, dict):
            raise_on_error(
                response,
                {"_raw_body": response.text},
            )
            raise TypeError(
                "Expected API response JSON to be an object"
            )

        data = cast(dict[str, Any], raw_data)

        raise_on_error(response, data)

        super().__init__(data)

        self.status_code = response.status_code
        self.headers = CaseInsensitiveDict(response.headers)

    @property
    def response_too_big(self) -> bool:
        """Whether the API marked the response as oversized."""
        return "x-response-too-big" in self.headers
