FROM python:2

RUN set -ex;\
    apt-get update;\
    apt-get install -y python-opencv

WORKDIR /usr/src/app
ADD read_camera.py ./
RUN pip install redis

CMD [ "python", "./read_camera.py" ]
