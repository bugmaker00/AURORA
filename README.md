# AURORA

**A**utonomous **U**nified **R**untime for **O**perations & **R**ecursive **A**utomation

AURORA is a modular Python framework for building composable, observable automation pipelines.

## Repository Layout

```
aurora/
├── core/          # Engine, scheduler, and utility helpers
├── adapters/      # Pluggable I/O adapters (HTTP, gRPC, …)
└── pipeline/      # Stage primitives and data transforms
```

## Quick Start

```bash
pip install -e .
python -c "import aurora; print(aurora.__version__)"
```

## Development

```bash
git checkout dev
pip install -r requirements-dev.txt
pytest
```

---

### 📝 Pending TODO Index

> Auto-generated from source. Every item below maps to an in-code `# TODO:` comment.

- `aurora/adapters/base.py:10` — define connection timeout parameter in base interface
- `aurora/adapters/base.py:19` — add message serialisation / compression support
- `aurora/adapters/http_adapter.py:15` — initialise requests.Session with retry configuration
- `aurora/adapters/http_adapter.py:19` — close and clean up the underlying HTTP session
- `aurora/adapters/http_adapter.py:23` — implement POST with configurable timeout and auth headers
- `aurora/adapters/http_adapter.py:24` — parse response and raise on non-2xx status codes
- `aurora/core/engine.py:13` — implement dynamic plugin loader via importlib
- `aurora/core/engine.py:17` — dispatch task to the correct worker based on task['type']
- `aurora/core/engine.py:18` — propagate cancellation token through worker chain
- `aurora/core/engine.py:22` — gracefully drain pending tasks before shutdown
- `aurora/core/scheduler.py:13` — add priority queue support
- `aurora/core/scheduler.py:17` — handle worker crashes and auto-restart failed tasks
- `aurora/core/utils.py:26` — implement exponential back-off retry decorator
- `aurora/core/utils.py:31` — add JSON-schema validation for the runtime config dict
- `aurora/core/utils.py:36` — strip workspace-absolute prefixes and return repo-relative path
- `aurora/pipeline/stage.py:15` — wrap handler execution in a try/except and emit metrics
- `aurora/pipeline/stage.py:30` — pass context through each stage in order; stop on failure
- `aurora/pipeline/stage.py:31` — record per-stage latency for observability
- `aurora/pipeline/transform.py:7` — handle list values inside nested dicts
- `aurora/pipeline/transform.py:20` — switch to Jinja2 for safe template rendering

### 🔎 Python Backlog Snapshot

> _Auto-generated 2026-04-10 19:35 UTC — do not edit manually._

Scanned **11** `.py` files on the `dev` branch; found **20 TODOs** and **0 FIXMEs** across **7** files. All outstanding items live in the adapters, core, and pipeline sub-packages — none are marked critical.

| file | TODOs | FIXMEs |
|------|------:|-------:|
| `aurora/adapters/base.py` | 2 | 0 |
| `aurora/adapters/http_adapter.py` | 4 | 0 |
| `aurora/core/engine.py` | 4 | 0 |
| `aurora/core/scheduler.py` | 2 | 0 |
| `aurora/core/utils.py` | 3 | 0 |
| `aurora/pipeline/stage.py` | 3 | 0 |
| `aurora/pipeline/transform.py` | 2 | 0 |
