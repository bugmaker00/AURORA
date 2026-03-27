"""Pipeline stage primitives."""
from dataclasses import dataclass, field
from typing import Any, Callable, Optional


@dataclass
class Stage:
    name: str
    handler: Callable
    retries: int = 0
    timeout: Optional[float] = None
    metadata: dict = field(default_factory=dict)

    def run(self, context: dict) -> Any:
        # TODO: wrap handler execution in a try/except and emit metrics
        return self.handler(context)


class Pipeline:
    """Ordered sequence of stages."""

    def __init__(self) -> None:
        self.stages: list[Stage] = []

    def add_stage(self, stage: Stage) -> "Pipeline":
        self.stages.append(stage)
        return self

    def execute(self, context: dict) -> dict:
        # TODO: pass context through each stage in order; stop on failure
        # TODO: record per-stage latency for observability
        for stage in self.stages:
            context = stage.run(context) or context
        return context
