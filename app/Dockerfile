# FROM python:3.7.3
FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive
ENV RUNTIME_DEPS "python3 python3-setuptools ca-certificates curl python3-opencv"

RUN set -ex;\
    apt-get update;\
    apt-get install -y --no-install-recommends $RUNTIME_DEPS;

RUN curl -q -s https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py; \
	python3 /tmp/get-pip.py

WORKDIR /app
ADD . /app

RUN pip3 install -r requirements.txt;

ENTRYPOINT [ "python3" ]
