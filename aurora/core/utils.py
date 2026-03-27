"""Utility helpers for AURORA core."""
import logging
from typing import Any, Optional


logger = logging.getLogger(__name__)


def setup_logging(level: str = "INFO") -> None:
    """Configure root logger."""
    logging.basicConfig(level=getattr(logging, level.upper(), logging.INFO))


def deep_merge(base: dict, override: dict) -> dict:
    """Recursively merge two dicts."""
    result = dict(base)
    for k, v in override.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result


def retry(fn, attempts: int = 3, delay: float = 1.0):
    # TODO: implement exponential back-off retry decorator
    pass


def validate_config(cfg: dict) -> bool:
    # TODO: add JSON-schema validation for the runtime config dict
    return True


def sanitize_path(p: str) -> str:
    # TODO: strip workspace-absolute prefixes and return repo-relative path
    return p
