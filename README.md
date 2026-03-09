# Python Actions Demo

Configuration samples with actions for Python projects.

## Environments

### Poetry

**Win**

```bash
pip install pipx
pipx install poetry
pipx list
pipx ensurepath
```

**Poetry first setup (once)**

```bash
poetry config virtualenvs.in-project true
poetry init
```

**Poetry routine**

```bash
poetry install
```

### pip

Store all requirements in file:

```bash
pip freeze requirements.txt > requirements.txt
```

## Tests

```bash
pytest tests # all
pytest -m book # Book only
pytest -m library # Library only
pytest -m "not slow" # all not slow
```
