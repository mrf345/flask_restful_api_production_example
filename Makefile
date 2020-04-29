test: install
	TESTING="True" python -m pytest --cov=./requester tests/*
lint: install
	TESTING="True" flake8 requester && flake8 tests
run: install
	DEVELOPEMENT="True" FLASK_APP="app" flask run
install:
	pip install --quiet -r requirements/test.txt
