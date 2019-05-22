FROM python:3.7.3

ENV RUNTIME_DEPS "python3-opencv"

RUN set -ex;\
    apt-get update;\
    apt-get install -y --no-install-recommends $RUNTIME_DEPS;

WORKDIR /app
ADD . /app

RUN set -ex; \
    pip3 install -r requirements.txt;

ENTRYPOINT [ "python3" ]
