FROM python:3.8-alpine
ADD . /sourcecode
WORKDIR /sourcecode
ENV FLASK_RUN_HOST 0.0.0.0
ENV DOCKER 'True'
ENV DEVELOPMENT 'True'
RUN pip install -r requirements/core.txt
CMD [ "flask", "run" ]
