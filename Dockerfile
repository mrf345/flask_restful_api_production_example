FROM python:3.8-alpine
ADD . /sourcecode
WORKDIR /sourcecode
ENV FLASK_RUN_HOST 0.0.0.0
ENV DOCKER 'True'
ENV FLASK_ENV 'development'
RUN pip install -r requirements/core.txt
CMD ./upgrade_db.sh && flask run
