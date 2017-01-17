FROM python:3.5

ENV PYTHONUNBUFFERED 1
MAINTAINER SciELO <scielo-dev@googlegroups.com>

RUN apt-get update \
    && apt-get install -qqy apt-utils \
    && apt-get install -qqy libxml2-utils

COPY ./requirements /requirements
RUN pip install -r /requirements/production.txt \
    && groupadd -r django \
    && useradd -r -g django django

RUN mkdir -p /etc/xml \
    && bash -c "$(curl -fsSL https://raw.githubusercontent.com/scieloorg/packtools/master/scripts/install_xml_catalog.sh)"

COPY . /app
RUN mkdir -p /app/media /app/static /app/logs
RUN chown -R django:django /app /app/media /app/static /app/logs \
    && chmod g+w /app/static /app/media /app/logs


COPY ./compose/django/gunicorn.sh /gunicorn.sh
COPY ./compose/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh \
    && sed -i 's/\r//' /gunicorn.sh \
    && chmod +x /entrypoint.sh \
    && chown django /entrypoint.sh \
    && chmod +x /gunicorn.sh \
    && chown django /gunicorn.sh

VOLUME ["/app/media", "/app/static"]

WORKDIR /app

USER django

ENTRYPOINT ["/entrypoint.sh"]
