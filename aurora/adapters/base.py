"""Base adapter interface."""
from abc import ABC, abstractmethod


class BaseAdapter(ABC):
    """Abstract base class for all AURORA adapters."""

    @abstractmethod
    def connect(self) -> None:
        # TODO: define connection timeout parameter in base interface
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @abstractmethod
    def send(self, payload: dict) -> dict:
        # TODO: add message serialisation / compression support
        pass
