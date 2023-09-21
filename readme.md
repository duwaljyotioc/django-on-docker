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
### Nginx
Nginx service is added to the docker-compose file.
Configurations for the nginx service can be found inside the nginx folder.
server_name should also be updated in the nginx file.

### Certbot
No additional configurations are required for the certbot.

### References:
1) https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
2) https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71


After deploying the app, you would need to hit the following commands:

1) docker-compose up --build
2) chmod +x init-letsencrypt.sh
3) sudo ./init-letsencrypt.sh

domains variable in the init-letsncrypt.sh should be replaced with the domain name for e.g
domains=(stinsonsinteriors.com www.stinsonsinteriors.com)

email should also be updated in the same file.
value of staging needs to be updated as well.
As there might be an exception thrown if there are too many tries with the staging off in the letsencrypt.sh
