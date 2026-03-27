"""Data transform helpers."""
from typing import Any


def flatten(data: dict, sep: str = ".") -> dict:
    """Flatten a nested dict."""
    # TODO: handle list values inside nested dicts
    result: dict = {}
    def _flatten(obj: Any, prefix: str = "") -> None:
        if isinstance(obj, dict):
            for k, v in obj.items():
                _flatten(v, f"{prefix}{k}{sep}" if prefix else f"{k}{sep}")
        else:
            result[prefix.rstrip(sep)] = obj
    _flatten(data)
    return result


def apply_template(template: str, context: dict) -> str:
    # TODO: switch to Jinja2 for safe template rendering
    return template.format(**context)
