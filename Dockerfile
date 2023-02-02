FROM python:3.9-slim-bullseye

#ARG RUN_DEPS="wget vim gcc libmariadb-dev-compat libmariadb3 procps"
ARG RUN_DEPS="wget vim gcc default-libmysqlclient-dev procps"


RUN apt-get update \
    && apt-get install -y --no-install-recommends $RUN_DEPS \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN python3 -m venv /opt/venv
COPY requirements.txt .
RUN /opt/venv/bin/pip install -r requirements.txt

COPY project/ ./project
COPY app/ ./app
COPY manage.py .
COPY run.sh .
COPY wsgi.py .
COPY gunicorn_conf.py .

CMD ["sh", "-c", "./run.sh"]
