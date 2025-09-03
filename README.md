# Diligent Learner

![Python](https://img.shields.io/badge/python-3.13-blue.svg) ![Ruff](https://img.shields.io/badge/style-ruff-%23cc66cc.svg?logo=ruff&logoColor=white) ![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)

Diligent Learner implementation

---

## Table of Contents

- [Requirements](#requirements)
- [Before You Start](#before-you-start)
- [Repository Structure](#repository-structure)
- [References](#references)

---

## Requirements

- Tested on **Fedora 42**
- Requires **Python 3.13**
- All dependencies are listed in [`pyproject.toml`](./pyproject.toml)

---

## Before You Start

To install all dependencies use [uv](https://docs.astral.sh/uv/)

for CPU-only:

```bash
uv sync --extra cpu
```

for CUDA 12.8:

```bash
uv sync --extra cu128
```

Optionally, enable pre-commit hooks for auto-formatting/linting:

```bash
uv run pre-commit install
```

To test that hook has successfully installed:

```bash
uv run pre-commit run --all-files
```

---

## Repository Structure

```text
.
├── data/                      # Data used in project
│   └── ...
|
├── materials/                  # Supplementary materials
│
├── src/                  # Python source files
│
├── .gitignore
├── .pre-commit-config.yaml    # Pre-commit hooks config
├── .python-version
├── pyproject.toml             # Dependency and tool config
├── README.md
└── uv.lock
```

---

## References

- [From Reasoning to Super-Intelligence: A Search-Theoretic Perspective](https://arxiv.org/abs/2507.15865)
