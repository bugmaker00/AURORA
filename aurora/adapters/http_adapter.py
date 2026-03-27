"""HTTP adapter implementation."""
import urllib.request
import json
from .base import BaseAdapter


class HTTPAdapter(BaseAdapter):
    """Adapter for plain HTTP endpoints."""

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self._session = None

    def connect(self) -> None:
        # TODO: initialise requests.Session with retry configuration
        pass

    def disconnect(self) -> None:
        # TODO: close and clean up the underlying HTTP session
        pass

    def send(self, payload: dict) -> dict:
        # TODO: implement POST with configurable timeout and auth headers
        # TODO: parse response and raise on non-2xx status codes
        return {}
