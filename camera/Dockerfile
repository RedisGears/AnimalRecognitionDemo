FROM python:2

WORKDIR /usr/src/app
ADD read_camera.py ./
RUN pip install opencv-python redis

CMD [ "python", "./read_camera.py" ]
