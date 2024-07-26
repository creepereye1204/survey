
FROM python:3.12.0-slim


WORKDIR /opt/Diabetes

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .



RUN set -xe \
    && apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2\
    && apt-get install -y --no-install-recommends build-essential \
    && pip install virtualenvwrapper poetry==1.4.2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


COPY ["poetry.lock", "pyproject.toml", "./"]
RUN poetry install --no-root


COPY ["Makefile", "./"]
COPY . .


EXPOSE 8080

CMD make run-server
