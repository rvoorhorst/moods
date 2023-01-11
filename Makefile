install:
	pip install -r requirements.txt

format:
	black .
	isort .

lint:
	black --check --diff .
	isort --check-only --diff .

migrate:
	manage.py migrate