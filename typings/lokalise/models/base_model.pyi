from typing import Any, ClassVar

class BaseModel:
    # class-level meta
    ATTRS: ClassVar[tuple[str, ...]]
    COMMON_ATTRS: ClassVar[tuple[str, ...]]
    DATA_KEY: ClassVar[str]

    raw_data: dict[str, Any]

    project_id: str | None
    user_id: int | None
    branch: str | None
    team_id: int | None

    def __init__(self, raw_data: dict[str, Any]) -> None: ...
    def __str__(self) -> str: ...
