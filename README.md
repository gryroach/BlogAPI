# Blog API

## Description

Django REST API project for blog. 
The service has endpoints for working with articles and comments for them.
There is functionality to add a reply to a comment in the form of another comment.

Data is recorded in the PostreSQL database.

***
## Getting started

### Clone remote files

```sh
$ git clone https://github.com/gryroach/BlogAPI.git
$ cd BlogAPI
```
### Create a virtual environment to install dependencies in and activate it:
```sh
$ pip install virtualenv
$ python3 -m venv env
$ source env/bin/activate
```
### Install the dependencies for django project:
```sh
(env)$ pip install -r .web/requirements.txt
```
### Create .env file to configure database settings:
```sh
(env)$ touch .env
(env)$ nano .env
```
### Set the following environment variables:
- ```SECRET_KEY```
- ```DEBUG```
- ```ALLOWED_HOSTS```
- ```POSTGRES_NAME```
- ```POSTGRES_USER```
- ```POSTGRES_PASSWORD```

### Run docker-compose
```sh
(env)$ docker-compose up --build -d
```
### Make migrations for Postgres database
```sh
(env)$ docker-compose exec web python manage.py makemigrations
(env)$ docker-compose exec web python manage.py migrate
```
***

### API
- GET -> http://{{host}}:8000/api/article/all - get all articles with comments ids
- POST -> http://{{host}}:8000/api/article/all - create new article
- GET -> http://{{host}}:8000/api/article/{{id}} - get article data by id with all comments
- GET -> http://{{host}}:8000/api/article/3level-comment/{{id}} - get article data by id with comments up to the third nesting level
- GET -> http://{{host}}:8000/api/comment/all - get all comments with all replies
- POST -> http://{{host}}:8000/api/comment/add/to-article - create new comment for article
- POST -> http://{{host}}:8000/api/comment/add/to-comment - create new reply for comment
- GET -> http://{{host}}:8000/api/comment/3-level - get all comments with third nesting level with all replies


To get a description of the developed API in Swagger UI format, follow the documentation link:
http://{{host}}:8000/api/docs/
