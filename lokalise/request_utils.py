"""
lokalise.request_utils
~~~~~~~~~~~~~~~~~~~~~~
This module provides helpers to send HTTP requests.
"""

import json
from typing import Any, Optional, Dict, NoReturn
from requests import Response
from lokalise import errors


def raise_on_error(response: Response, data: Dict[str, Any]) -> None:
    """Raises an error for HTTP codes 400+
    """
    if response.status_code > 399 or 'error' in data:
        respond_with_error(data, response.status_code)


def respond_with_error(data: Dict[str, Any], code: Any) -> NoReturn:
    """Raises an error based on the HTTP status code.
    If the status code is unknown, raises a generic ClientError

    :param data: Response body from the API that usually contains error message
    :param code: Response status code
    """
    msg: str = ''
    if 'error' in data:
        msg = data['error']
        if isinstance(msg, Dict):
            msg = msg['message']
    else:
        msg = data['message']

    if code in errors.ERROR_CODES:
        raise errors.ERROR_CODES[code](msg, code)

    raise errors.ClientError(msg, code)


def __format_params(params: Optional[Dict] = None) -> Optional[str]:
    """Converts request params to JSON
    """
    return json.dumps(params) if params else None


def __prepare(path: str) -> str:
    """Prepares the URI by stripping all unnecessary slashes
    """
    return path.strip('/')
