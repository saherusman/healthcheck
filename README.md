[![CI](https://github.com/saherusman/healthcheck/actions/workflows/ci.yml/badge.svg)](https://github.com/saherusman/healthcheck/actions/workflows/ci.yml)
# Healthcheck

A simple Python tool that checks disk usage and reports whether the disk is healthy.

## Features

- Checks disk usage for a selected path.
- Displays disk usage as a percentage.
- Reports disk status: `OK`, `WARN`, or `CRIT`.
- Supports human-readable output.
- Supports JSON output using `--json`.

## Requirements

- Python 3
- pytest (for running tests)
- Ruff (for code checks)

## Usage

Check disk usage on the root filesystem:

```bash
python3 healthcheck.py
```

Check disk usage for a selected path:

```bash
python3 healthcheck.py [path]
```

Display output in JSON format:

```bash
python3 healthcheck.py --json
```

## Testing

Run the tests using pytest:

```bash
pytest -v
```

## Code Quality

Run Ruff to check the code:

```bash
ruff check .
```
ok
