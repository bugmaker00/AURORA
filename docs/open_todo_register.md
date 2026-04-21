# Open TODO Register

Scanned branch: `dev`  
Repository: `bugmaker00/AURORA`  
Tracked `.py` files examined: 11  
Open TODO items found: 20

Each bullet lists the relative file path, the line number, and the exact TODO text.
TODOs whose feature was already implemented in the surrounding code are excluded.

- `aurora/adapters/base.py` line 10: `# TODO: define connection timeout parameter in base interface`
- `aurora/adapters/base.py` line 19: `# TODO: add message serialisation / compression support`
- `aurora/adapters/http_adapter.py` line 15: `# TODO: initialise requests.Session with retry configuration`
- `aurora/adapters/http_adapter.py` line 19: `# TODO: close and clean up the underlying HTTP session`
- `aurora/adapters/http_adapter.py` line 23: `# TODO: implement POST with configurable timeout and auth headers`
- `aurora/adapters/http_adapter.py` line 24: `# TODO: parse response and raise on non-2xx status codes`
- `aurora/core/engine.py` line 13: `# TODO: implement dynamic plugin loader via importlib`
- `aurora/core/engine.py` line 17: `# TODO: dispatch task to the correct worker based on task['type']`
- `aurora/core/engine.py` line 18: `# TODO: propagate cancellation token through worker chain`
- `aurora/core/engine.py` line 22: `# TODO: gracefully drain pending tasks before shutdown`
- `aurora/core/scheduler.py` line 13: `# TODO: add priority queue support`
- `aurora/core/scheduler.py` line 17: `# TODO: handle worker crashes and auto-restart failed tasks`
- `aurora/core/utils.py` line 26: `# TODO: implement exponential back-off retry decorator`
- `aurora/core/utils.py` line 31: `# TODO: add JSON-schema validation for the runtime config dict`
- `aurora/core/utils.py` line 36: `# TODO: strip workspace-absolute prefixes and return repo-relative path`
- `aurora/pipeline/stage.py` line 15: `# TODO: wrap handler execution in a try/except and emit metrics`
- `aurora/pipeline/stage.py` line 30: `# TODO: pass context through each stage in order; stop on failure`
- `aurora/pipeline/stage.py` line 31: `# TODO: record per-stage latency for observability`
- `aurora/pipeline/transform.py` line 7: `# TODO: handle list values inside nested dicts`
- `aurora/pipeline/transform.py` line 20: `# TODO: switch to Jinja2 for safe template rendering`
