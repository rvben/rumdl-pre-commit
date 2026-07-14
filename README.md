# rumdl-pre-commit

A [pre-commit](https://pre-commit.com/) hook for [rumdl](https://github.com/rvben/rumdl), a fast Markdown linter and formatter written in Rust.

## Usage

To use rumdl with pre-commit, add the following to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/rvben/rumdl-pre-commit
    rev: v0.2.34
    hooks:
      - id: rumdl      # Lint only; add args [--fix] to auto-fix
      - id: rumdl-fmt  # Pure format, always exits 0
```

Two hooks are available:
- **`rumdl`** - Lints files and exits 1 if violations are found. Non-destructive by default; add `args: [--fix]` to auto-fix in place (the same opt-in model as ruff's linter hook).
- **`rumdl-fmt`** - Formats files in place and always exits 0. Relies on pre-commit's file-change detection. Use alongside `rumdl` for the ruff-style split.

To auto-fix violations in place, opt in with `args`:

```yaml
      - id: rumdl
        args: [--fix]
```

## Installation

When you run `pre-commit install` or `pre-commit run`, pre-commit will automatically install `rumdl` in an isolated Python environment using pip. You do **not** need to install rumdl manually.

## License

MIT (see [LICENSE](LICENSE)) 