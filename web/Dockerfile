FROM python:3.9

# copy project
COPY ./config src/web/config
COPY ./blog src/web/blog
COPY manage.py src/web/

# set work directory
WORKDIR /src/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
