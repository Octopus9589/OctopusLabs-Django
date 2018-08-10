FROM python:3.7-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache git build-base linux-headers libffi-dev mariadb-dev \
    gettext curl gcc musl-dev python3-dev libressl-dev perl postgresql \
    postgresql-dev libpq

RUN mkdir -p /opt/app

ENV TERM=xterm APP=/opt/app

WORKDIR $APP

ADD Pipfile Pipfile.lock $APP/

RUN pip install pipenv

RUN pipenv install --system

ADD . $APP/

CMD ["sh", "run-prod.sh"]
