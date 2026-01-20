# rumdl-pre-commit

A [pre-commit](https://pre-commit.com/) hook for [rumdl](https://github.com/rvben/rumdl), a fast Markdown linter and formatter written in Rust.

## Usage

To use rumdl with pre-commit, add the following to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/rvben/rumdl-pre-commit
    rev: v0.0.222
    hooks:
      - id: rumdl      # Lint only (fails on issues)
      - id: rumdl-fmt  # Auto-format and fail if issues remain
```

Two hooks are available:
- **`rumdl`** — Lints files and fails if any issues are found
- **`rumdl-fmt`** — Auto-formats files and fails if unfixable violations remain (recommended for CI)

## Installation

When you run `pre-commit install` or `pre-commit run`, pre-commit will automatically install `rumdl` in an isolated Python environment using pip. You do **not** need to install rumdl manually.

## License

MIT (see [LICENSE](LICENSE)) 