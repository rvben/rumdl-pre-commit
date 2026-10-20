# rumdl-pre-commit

A [pre-commit](https://pre-commit.com/) hook for [rumdl](https://github.com/rvben/rumdl), a fast Markdown linter and formatter written in Rust.

## Usage

To use rumdl with pre-commit, add the following to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/rvben/rumdl-pre-commit
    rev: v0.3.0
    hooks:
      - id: rumdl-check  # Lint only; add args [--fix] to auto-fix
      - id: rumdl-fmt    # Format in place
```

The recommended hooks are:

- **`rumdl-check`** - Lints files and exits 1 if violations are found. Non-destructive by default; add `args: [--fix]` to auto-fix in place and fail if violations remain (the same opt-in model as ruff's linter hook).
- **`rumdl-fmt`** - Formats files in place and exits 0 for remaining lint violations. Relies on pre-commit's file-change detection. Use alongside `rumdl-check` for the ruff-style split. Execution and configuration errors can still cause a nonzero exit.

The legacy **`rumdl`** ID remains available as an alias for `rumdl-check`; existing configurations do not need to change.

### Fix and check remaining violations

For a single hook that applies fixes and fails if unfixable violations remain, use:

```yaml
      - id: rumdl-check
        args: [--fix]
```

Pre-commit also fails the run when a hook changes files, so review and stage the fixes before committing again.

### Passing options

The `rumdl-check` hook runs `rumdl check` and `rumdl-fmt` runs `rumdl fmt`; pass any flag of that command through `args`. For example, to auto-fix in place and skip the configured [code-block tools](https://rumdl.dev/code-block-tools/):

```yaml
      - id: rumdl-check
        args: [--fix, --no-code-block-tools]
```

See the [pre-commit page in the rumdl docs](https://rumdl.dev/usage/pre-commit/) for more examples, including the code-block tool modes.

## Installation

When you run `pre-commit install` or `pre-commit run`, pre-commit will automatically install `rumdl` in an isolated Python environment using pip. You do **not** need to install rumdl manually.

## License

MIT (see [LICENSE](LICENSE))
