# pull base image
FROM python:3.12.7-slim-bullseye


# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

# set working directory
WORKDIR /app



# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .