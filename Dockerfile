# Building docker image procedure

FROM python:3.9-slim

LABEL maintainer="harksodje@gmail.com"
RUN echo "python docker image"
# System deps:
RUN pip install poetry
# The directory for images
WORKDIR /project
# copy requirements files for dependency
COPY ./pyproject.toml .
COPY ./poetry.lock .
RUN poetry install
# project initialization
RUN poetry config virtualenvs.create false
COPY . .
# RUN poetry shell
CMD [ "poetry","run", "python", "demo/manage.py", "runserver", "0.0.0.0:8000", ]
