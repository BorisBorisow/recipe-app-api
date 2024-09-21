# Use the official Python image based on Alpine Linux
FROM python:3.9-alpine3.13

# Maintainer label (optional, but good practice)
LABEL maintainer="bborrisow.com"

# Environment variable to keep Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Copy the requirements file to a temporary location
COPY ./requirements.txt /tmp/requirements.txt

# Copy the application code to the /app directory
COPY ./app /app

# Set the working directory to /app
WORKDIR /app

# Expose port 8000 (default port for Django)
EXPOSE 8000

# Install dependencies in a virtual environment
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt && \
    adduser \  
        --disabled-password \
        --no-create-home \
        django-user

# Set the PATH environment variable to use the virtual environment
ENV PATH="/py/bin:$PATH"

# Switch to the newly created user
USER django-user
