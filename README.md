# Python Backend Journey

This repository tracks my backend learning work in Python.

## Week 2 Focus

- Use the terminal confidently.
- Understand files, directories, and paths.
- Create and activate a virtual environment.
- Track dependencies.
- Use a standard Python project layout.
- Use Git for commits.
- Push the project to GitHub.

## Project Layout

```text
python-backend-journey/
├── README.md
├── pyproject.toml
├── src/
│   └── backend_journey/
│       ├── __init__.py
│       └── health.py
└── tests/
    └── test_health.py
```

## Local Commands

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Run tests:

```bash
PYTHONPATH=src python -m unittest
```

Deactivate the virtual environment:

```bash
deactivate
```## Notes

This project uses a virtual environment and pytest for testing.

