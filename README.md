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

- `/workspace/agent_workspace/archive/AURORA/aurora/core/utils.py:26` — implement exponential back-off retry decorator
- `/workspace/agent_workspace/archive/AURORA/aurora/core/utils.py:31` — add JSON-schema validation for the runtime config dict
- `/workspace/agent_workspace/archive/AURORA/aurora/core/utils.py:36` — strip workspace-absolute prefixes and return repo-relative path
- `/workspace/agent_workspace/archive/AURORA/aurora/core/engine.py:13` — implement dynamic plugin loader via importlib
- `/workspace/agent_workspace/archive/AURORA/aurora/core/engine.py:17` — dispatch task to the correct worker based on task['type']
- `/workspace/agent_workspace/archive/AURORA/aurora/core/engine.py:18` — propagate cancellation token through worker chain
- `/workspace/agent_workspace/archive/AURORA/aurora/core/engine.py:22` — gracefully drain pending tasks before shutdown
- `/workspace/agent_workspace/archive/AURORA/aurora/core/scheduler.py:13` — add priority queue support
- `/workspace/agent_workspace/archive/AURORA/aurora/core/scheduler.py:17` — handle worker crashes and auto-restart failed tasks
- `/workspace/agent_workspace/archive/AURORA/aurora/adapters/base.py:10` — define connection timeout parameter in base interface
- `/workspace/agent_workspace/archive/AURORA/aurora/adapters/base.py:19` — add message serialisation / compression support
- `/workspace/agent_workspace/archive/AURORA/aurora/adapters/http_adapter.py:15` — initialise requests.Session with retry configuration
- `/workspace/agent_workspace/archive/AURORA/aurora/adapters/http_adapter.py:19` — close and clean up the underlying HTTP session
- `/workspace/agent_workspace/archive/AURORA/aurora/adapters/http_adapter.py:23` — implement POST with configurable timeout and auth headers
- `/workspace/agent_workspace/archive/AURORA/aurora/adapters/http_adapter.py:24` — parse response and raise on non-2xx status codes
- `/workspace/agent_workspace/archive/AURORA/aurora/pipeline/stage.py:15` — wrap handler execution in a try/except and emit metrics
- `/workspace/agent_workspace/archive/AURORA/aurora/pipeline/stage.py:30` — pass context through each stage in order; stop on failure
- `/workspace/agent_workspace/archive/AURORA/aurora/pipeline/stage.py:31` — record per-stage latency for observability
- `/workspace/agent_workspace/archive/AURORA/aurora/pipeline/transform.py:7` — handle list values inside nested dicts
- `/workspace/agent_workspace/archive/AURORA/aurora/pipeline/transform.py:20` — switch to Jinja2 for safe template rendering
