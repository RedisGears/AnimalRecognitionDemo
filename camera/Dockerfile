FROM python:2

RUN pip install -q opencv-python redis

WORKDIR /usr/src/app

ADD read_camera.py ./
ADD *.jpg ./

CMD [ "python", "./read_camera.py" ]
