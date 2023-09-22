# Use an official Python runtime as a parent image
FROM python:3.10-alpine

# Set the working directory to /usr/src/app
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Add a user with UID 1000 and GID 1000
RUN adduser -D -u 1000 -g 1000 app

# Create the log directory and adjust permissions
RUN mkdir -p /app/logs \
    && chown -R app:app /app/logs \
    && chmod -R 755 /app/logs

# Set the HOME environment variable
ENV HOME /home/app

# Add the user's local bin directory to the PATH
ENV PATH "$PATH:/home/app/.local/bin"

# temporarily switch to root user
USER root
RUN chown -R app:app /app

# Switch to the 'app' user
USER app

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file
COPY ./requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt


# Copy the project files
COPY ./ /app