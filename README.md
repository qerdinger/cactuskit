# CactusKIT

Lightweight Python SDK for declaring small API handlers and producing consistent responses.

See package metadata in `pyproject.toml`.

## Quick links

- Source: https://github.com/qerdinger/cactuskit
- Requires: Python 3.10+

## Overview

CactusKIT provides a single-purpose decorator `cactuize` to declare API entrypoints and a
small response wrapper `CactusResponse` so handlers return consistent, serializable objects.

Key pieces:

- `cactuize(...)` : decorator that validates/binds args, optionally enforces `auth`, and
  normalizes return values into `CactusResponse`.
- `CactusResponse` / `make_res()` : response object and factory with helpers (size, hash, timestamp).
- `CactusEncoder` : JSON encoder that can serialize `CactusResponse` instances.
- Enums: `HttpStatus`, `ApiProtocol`, `ApiMethod`.

## Installation

Install from source or PyPI when available:

```bash
pip install cactuskit
```

## Usage

Import the symbols from the module and declare handlers with `cactuize`.

```python
from cactuskit import ApiMethod, ApiProtocol, HttpStatus, cactuize

def authenticate():
    return True

@cactuize()
def simple_entrypoint():
    return f"Hello World from {simple_entrypoint}"

@cactuize(
    auth=authenticate,
    protocol=ApiProtocol.HTTP,
    method=ApiMethod.GET)
def entrypoint(name):
    return (HttpStatus.HTTP_CUSTOM(201), {
        "content": f"Hello {name}"
    })
```

Notes:
- Handler functions may return a plain payload (`dict` or `str`) or a tuple `(HttpStatus, payload)`.
- If `auth` is provided to `cactuize`, it should be a callable returning truthy when authorized.

## API Reference (short)

- `cactuize(protocol=ApiProtocol, method=ApiMethod, auth=None, middleware=None, args_mtable=None)`
  : declare a function as a Cactus entrypoint. Performs argument binding and converts results into
  `CactusResponse` objects. When `auth` is provided, it is called and a failed check returns a
  plain "Authentication required" string.
- `CactusResponse(payload, status_code)` : wrapper with helpers: `get_payload()`, `get_status_code()`,
  `get_timestamp()`, `get_payload_size()`, `get_payload_hash()`.
- `make_res(payload, status_code=HttpStatus.HTTP_OK)` : helper factory.
- `CactusEncoder` : `json.JSONEncoder` subclass that serializes `CactusResponse` instances.

## Development

- Create a virtualenv and install dev dependencies (if any).

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Contributing

Contributions welcome. Open issues or pull requests and include tests for new behavior.

## License

MIT : see [LICENSE](https://raw.githubusercontent.com/qerdinger/cactuskit/refs/heads/main/LICENSE).