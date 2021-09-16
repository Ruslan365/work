# pull official base image
FROM python:3.6
# set work directory
WORKDIR work-rus_rework
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip3 install --upgrade pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
# copy project
COPY . .