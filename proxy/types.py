from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class ProxyType(Enum):
    HTTP = 'http'
    HTTPS = 'https'
    SOCKS4 = 'socks4'
    SOCKS5 = 'socks5'


@dataclass
class Proxy:
    value: str
    type: ProxyType


class ProxyProvider(ABC):
    @abstractmethod
    def provide_proxies(self, with_type: bool | None = True) -> list[Proxy] | list[str]:
        pass


class ProvideProxyException(RuntimeError):
    pass
