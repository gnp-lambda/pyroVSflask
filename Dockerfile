FROM python:2.7-slim

ADD requirements.txt /
RUN pip install -r /requirements.txt

RUN mkdir -p /app
WORKDIR /app
ADD . /app
