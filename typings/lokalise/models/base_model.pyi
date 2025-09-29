from typing import Any, ClassVar

class BaseModel:
    # class-level meta
    ATTRS: ClassVar[list[str]]
    COMMON_ATTRS: ClassVar[list[str]]
    DATA_KEY: ClassVar[str]

    raw_data: dict[str, Any]

    def __init__(self, raw_data: dict[str, Any]) -> None: ...
    def __str__(self) -> str: ...
    def __extract_common_attrs(self, raw_data: dict[str, Any]) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
