install:
	poetry install
lint:
	poetry run flake8 --ignore=I002,T001 brain_games