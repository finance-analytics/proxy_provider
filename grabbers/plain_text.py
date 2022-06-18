from typing import Optional, Union

import requests

from grabbers.types import ProxyProvider, Proxy, ProvideProxyException, ProxyType


class PlainTextProxyProvider(ProxyProvider):
    def __init__(self, url: str, proxy_type: ProxyType, delimiter: Optional[str] = '\n') -> None:
        self._url = url
        self._proxy_type = proxy_type
        self._delimiter = delimiter

    def provide_proxies(self, with_type: Optional[bool] = True) -> Union[list[Proxy], list[str]]:
        try:
            request = requests.get(url=self._url)
            proxies = request.text.split(self._delimiter)
            if with_type:
                return [Proxy(value=value_, type=self._proxy_type) for value_ in proxies]
            return proxies
        except requests.exceptions.RequestException as exception:
            raise ProvideProxyException(str(exception))
