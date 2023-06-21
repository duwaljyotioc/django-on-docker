Create a django app with virtual environment first.


Create a requirement.txt with the pip freeze command.
pip freeze > requirements.txt

Lets assume that the project main folder name is: app.
Create a file called Dockerfile in the app with the below contents

```
# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /usr/src/app
In a Dockerfile, the WORKDIR instruction is used to set the working directory for any subsequent instructions 
that follow it. It is used to define the directory inside the Docker container where commands,
 such as RUN, CMD, and COPY, are executed or relative paths are resolved.

# set environment variables
#  Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

#ENTRYPOINT sh -c "python manage.py migrate"
```


Create a docker-compose file with the below contents:

```
version: '3.8'

services:
  web:
    build: ./app
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ./app/:/usr/src/app/
    ports:
      - 8000:8000
    env_file:
      - ./.env.dev
    depends_on:
      - db
  db:
    image: postgres:13.0-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_USER=hello_django
      - POSTGRES_PASSWORD=hello_django
      - POSTGRES_DB=hello_django_dev

volumes:
  postgres_data:

```
