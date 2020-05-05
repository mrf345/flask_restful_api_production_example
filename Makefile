test: install
	FLASK_ENV="testing" TESTING="True" python -m pytest --cov=./requester tests/*
lint: install
	FLASK_ENV="testing" TESTING="True" flake8 requester && flake8 tests
run: install
	FLASK_ENV="development" FLASK_APP="app" flask run
install:
	pip install --quiet -r requirements/test.txt
