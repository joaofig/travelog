
setup:
	uv init --app --description "eVED Web-based viewer" --python 3.13
	uv sync
	uv run python -m ensurepip --upgrade


run:
	uv run main.py

check:
	uvx ruff check .


format:
	uvx ruff format .
	uvx ruff check . --fix
	uvx ruff check --select I . --fix
