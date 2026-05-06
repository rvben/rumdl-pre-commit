# rumdl-pre-commit

A [pre-commit](https://pre-commit.com/) hook for [rumdl](https://github.com/rvben/rumdl), a fast Markdown linter and formatter written in Rust.

## Usage

To use rumdl with pre-commit, add the following to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/rvben/rumdl-pre-commit
    rev: v0.1.89
    hooks:
      - id: rumdl      # Lint + auto-fix, fails if unfixable issues remain
      - id: rumdl-fmt  # Pure format, always exits 0
```

Two hooks are available:
- **`rumdl`** — Lints and auto-fixes files. Exits 1 if unfixable violations remain. Use this for full coverage.
- **`rumdl-fmt`** — Formats files in place and always exits 0. Relies on pre-commit's file-change detection. Use alongside `rumdl` for the ruff-style split.

## Installation

When you run `pre-commit install` or `pre-commit run`, pre-commit will automatically install `rumdl` in an isolated Python environment using pip. You do **not** need to install rumdl manually.

## License

MIT (see [LICENSE](LICENSE)) 