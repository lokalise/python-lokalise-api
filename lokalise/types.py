from typing import Protocol, TypeAlias

Number: TypeAlias = int | float


class RequestClientProto(Protocol):
    @property
    def token_header(self) -> str: ...

    @property
    def token(self) -> str | None: ...

    @property
    def enable_compression(self) -> bool: ...

    @property
    def connect_timeout(self) -> Number | None: ...

    @property
    def read_timeout(self) -> Number | None: ...


class HasApiHost(Protocol):
    @property
    def api_host(self) -> str | None: ...


class FullClientProto(RequestClientProto, HasApiHost, Protocol):
    pass
