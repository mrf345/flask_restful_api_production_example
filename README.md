## Flask restful API production example
There's a [live demo](https://925b1pnu98.execute-api.us-east-2.amazonaws.com/production) of the project hosted on AWS Lambda functions.

### Setup
###### - With docker:
Make sure `docker` and `docker-compose` are installed and run `docker-compose up`

###### - Or from the source instead:
Make sure `Python 3.7` and `pip` are installed and then:
- `pip install -r requirements/core.py`
- `DEVELOPEMENT="True" FLASK_APP="app" flask run`

###### - To run tests and linting
- Tests `make tests`
- Linting `make lint`

### Intro
###### - Features and Stack
- Swagger OpenAPI2 API with `Flask-Restx`
- Database migration with `Flask-Migrate`
- Containerized local dev environment with `Docker`
- AWS RDS and lambda deployment ready with `Zappa`
- Errors monitoring and reporting with `Sentry`
- Github actions testing, linting and deployment with `PyTest` and `Flake8`. 

###### - Project structure
<pre>
.
├── app.py
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── Makefile
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
├── README.md
├── requester
│   ├── api
│   │   ├── auth.py
│   │   ├── endpoints
│   │   │   ├── features.py
│   │   │   ├── __init__.py
│   │   │   └── users.py
│   │   ├── __init__.py
│   │   ├── limiter.py
│   │   └── setup.py
│   ├── constants.py
│   ├── database
│   │   ├── defaults.py
│   │   ├── __init__.py
│   │   ├── mixins.py
│   │   ├── models.py
│   │   ├── relations.py
│   │   └── setup.py
│   ├── database.db
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── requirements
│   ├── core.txt
│   └── test.txt
├── tests
│   ├── features.py
│   ├── __init__.py
│   └── users.py
└── zappa_settings.json
</pre>


#### TODOS
- [x] Add flask-migration
- [x] Add couple of tests with pytest
- [x] Add a docker-compose with mysql with a volume
- [x] Add Sentry
- [x] Setup RDS with mysql and lambda
- [x] Add github CI action
- [x] Add README.md with instructions
- [ ] Add test and coverage badges
- [ ] Add github AWS deploy action 
- [ ] Update folder structure
