test: install
	TESTING="True" pytest --cov=./requester tests/*
lint: install
	TESTING="True" flake8 requester
run: install
	DEVELOPEMENT="True" FLASK_APP="app" flask run
install:
	pip install --quiet -r requirements/test.txt
