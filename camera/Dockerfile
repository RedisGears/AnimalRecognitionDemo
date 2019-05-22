FROM python:2

ENV RUNTIME_DEPS "python-opencv"

RUN set -ex;\
    apt-get update;\
    apt-get install -y --no-install-recommends $RUNTIME_DEPS;

WORKDIR /usr/src/app
ADD read_camera.py ./
RUN pip install redis

CMD [ "python", "./read_camera.py" ]
