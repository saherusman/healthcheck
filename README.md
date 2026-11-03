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
