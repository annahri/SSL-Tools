FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN useradd --create-home -U apps 

WORKDIR /app/
COPY --chown=apps:apps . .

RUN pip install pipenv

USER apps:apps
RUN pipenv install --deploy --clear

WORKDIR /app/src/

EXPOSE 8000

ENTRYPOINT [ "pipenv", "run" ]
CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "ssl-tools.wsgi" ]

#ENTRYPOINT [ "bash", "-c" ]
#CMD [ "/app/docker/start.sh" ]
