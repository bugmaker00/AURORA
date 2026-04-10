# TODO Index — AURORA `dev` branch

> Auto-generated 2026-04-10 19:35 UTC. Scanned **11** `.py` files;
> found **20 TODOs** and **0 FIXMEs** (20 total).

---

## `aurora/adapters/base.py`

1. **[TODO]** Line 10: _define connection timeout parameter in base interface_
2. **[TODO]** Line 19: _add message serialisation / compression support_

## `aurora/adapters/http_adapter.py`

3. **[TODO]** Line 15: _initialise requests.Session with retry configuration_
4. **[TODO]** Line 19: _close and clean up the underlying HTTP session_
5. **[TODO]** Line 23: _implement POST with configurable timeout and auth headers_
6. **[TODO]** Line 24: _parse response and raise on non-2xx status codes_

## `aurora/core/engine.py`

7. **[TODO]** Line 13: _implement dynamic plugin loader via importlib_
8. **[TODO]** Line 17: _dispatch task to the correct worker based on task['type']_
9. **[TODO]** Line 18: _propagate cancellation token through worker chain_
10. **[TODO]** Line 22: _gracefully drain pending tasks before shutdown_

## `aurora/core/scheduler.py`

11. **[TODO]** Line 13: _add priority queue support_
12. **[TODO]** Line 17: _handle worker crashes and auto-restart failed tasks_

## `aurora/core/utils.py`

13. **[TODO]** Line 26: _implement exponential back-off retry decorator_
14. **[TODO]** Line 31: _add JSON-schema validation for the runtime config dict_
15. **[TODO]** Line 36: _strip workspace-absolute prefixes and return repo-relative path_

## `aurora/pipeline/stage.py`

16. **[TODO]** Line 15: _wrap handler execution in a try/except and emit metrics_
17. **[TODO]** Line 30: _pass context through each stage in order; stop on failure_
18. **[TODO]** Line 31: _record per-stage latency for observability_

## `aurora/pipeline/transform.py`

19. **[TODO]** Line 7: _handle list values inside nested dicts_
20. **[TODO]** Line 20: _switch to Jinja2 for safe template rendering_
