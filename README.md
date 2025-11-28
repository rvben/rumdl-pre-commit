# rumdl-pre-commit

A [pre-commit](https://pre-commit.com/) hook for [rumdl](https://github.com/rvben/rumdl), a fast Markdown linter and fixer written in Rust.

## Usage

To use rumdl with pre-commit, add the following to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/rvben/rumdl-pre-commit
    rev: v0.0.185  # Use the latest release tag
    hooks:
      - id: rumdl
        # To only check (default):
        # args: []
        # To automatically fix issues:
        # args: [--fix]
```

- By default, the hook will only check for issues.
- To automatically fix issues, add `args: [--fix]` to the hook configuration.

## Installation

When you run `pre-commit install` or `pre-commit run`, pre-commit will automatically install `rumdl` in an isolated Python environment using pip. You do **not** need to install rumdl manually.

## License

MIT (see [LICENSE](LICENSE)) 