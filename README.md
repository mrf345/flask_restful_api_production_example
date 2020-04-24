# Lambda Production Ready Flask Restful API Example

### Features and Stack
- Token Authentication
- Swagger OpenAPI2
- Containerized local dev environment
- AWS RDS and lambda deployment
- Github actions testing, linting and deployment  


### Introduction
###### Files structure
<pre>
.
├── docker-compose.yml
├── requester
│   ├── api
│   │   ├── auth.py
│   │   ├── endpoints
│   │   │   ├── features.py
│   │   │   ├── __init__.py
│   │   │   └── users.py
│   │   ├── __init__.py
│   │   └── setup.py
│   ├── app.py
│   ├── constants.py
│   ├── database
│   │   ├── defaults.py
│   │   ├── __init__.py
│   │   ├── mixins.py
│   │   ├── models.py
│   │   ├── relations.py
│   │   └── setup.py
│   ├── __init__.py
│   └── utils.py
├── requirements
│   ├── core.txt
│   └── main.txt
└── todo.md
</pre>


#### TODOS
- [ ] Add flask-migration
- [ ] Add couple of tests with pytest
- [ ] Add a docker-compose with mysql with a volume
- [ ] Add code to a github repo!
- [ ] Setup RDS with mysql and lambda
- [ ] Add github actions with AWS secrets
- [ ] Add README.md with instructions
