from typing import Protocol


class RequestClientProto(Protocol):
    @property
    def token_header(self) -> str: ...
    @property
    def token(self) -> str | None: ...
    @property
    def enable_compression(self) -> bool | None: ...
    @property
    def connect_timeout(self) -> float | int | None: ...
    @property
    def read_timeout(self) -> float | int | None: ...


class HasApiHost(Protocol):
    @property
    def api_host(self) -> str | None: ...


class FullClientProto(RequestClientProto, HasApiHost, Protocol):
    pass
