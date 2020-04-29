
<h2 align='center'>Flask restful API production example</h2>
<p align='center'>
    There's a <a href='https://925b1pnu98.execute-api.us-east-2.amazonaws.com/production'>live demo</a> of the project hosted on AWS Lambda functions.
    <br /><br />
    <a href='https://github.com/mrf345/flask_restful_api_production_example/actions' target='_blank' style='margin-right: 2%'>
        <img alt='Actions Status' src='https://github.com/mrf345/flask_restful_api_production_example/workflows/CI/badge.svg' />
    </a>
    <a href='https://coveralls.io/github/mrf345/flask_restful_api_production_example?branch=master'>
        <img src='https://coveralls.io/repos/github/mrf345/flask_restful_api_production_example/badge.svg?branch=master' alt='Coverage Status' />
    </a>
</p>


### Setup
##### - With docker:
Make sure `docker` and `docker-compose` are installed and run `docker-compose up`

##### - Or from the source instead:
Make sure `Python 3.7` and `pip` are installed and then:
- `pip install -r requirements/core.py`
- `DEVELOPEMENT="True" FLASK_APP="app" flask run`

##### - To run tests and linting
- Tests `make tests`
- Linting `make lint`

### Intro
##### - Features and Stack
- Swagger OpenAPI2 API with `Flask-Restx`
- Database migration with `Flask-Migrate`
- Containerized local dev environment with `Docker`
- AWS RDS and lambda deployment ready with `Zappa`
- Errors monitoring and reporting with `Sentry`
- Github actions testing, linting and deployment with `PyTest` and `Flake8`. 


##### - Project structure
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
│   ├── README.md
│   ├── script.py.mako
│   └── versions
│       └── d826e674004f_.py
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
│   ├── config.py
│   ├── constants.py
│   ├── database
│   │   ├── defaults.py
│   │   ├── __init__.py
│   │   ├── mixins.py
│   │   ├── models.py
│   │   ├── relations.py
│   │   └── setup.py
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── requirements
│   ├── core.txt
│   ├── deploy.txt
│   └── test.txt
├── tests
│   ├── conftest.py
│   ├── features.py
│   ├── __init__.py
│   └── users.py
├── upgrade_db.sh
└── zappa_settings.json
</pre>
