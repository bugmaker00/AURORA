"""Task scheduler."""
import asyncio
from typing import Callable, Coroutine


class Scheduler:
    """Async task scheduler."""

    def __init__(self) -> None:
        self._queue: asyncio.Queue = asyncio.Queue()

    async def enqueue(self, coro: Coroutine) -> None:
        # TODO: add priority queue support
        await self._queue.put(coro)

    async def run_forever(self) -> None:
        # TODO: handle worker crashes and auto-restart failed tasks
        while True:
            coro = await self._queue.get()
            await coro
