install:
	 uv add -r requirements.txt && uv sync

format:
	uv run black Python/stock-trading-app/*.py

lint:
	uv run pylint Python/stock-trading-app/*py


all:
	install format lint