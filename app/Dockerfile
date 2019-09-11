# FROM python:3.7.3
FROM debian:buster

ENV DEBIAN_FRONTEND=noninteractive
ENV RUNTIME_DEPS "python3 python3-setuptools ca-certificates curl python3-opencv"

RUN set -ex ;\
    apt-get -qq update ;\
    apt-get -q install -y --no-install-recommends $RUNTIME_DEPS

RUN set -ex ;\
	curl -q -s https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py ;\
	python3 /tmp/get-pip.py

WORKDIR /app
ADD . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]
