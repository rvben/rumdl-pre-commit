fmt:
	ruff check --fix .
	ruff format .

mirror:
	@uv run mirror.py
