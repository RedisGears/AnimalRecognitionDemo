# AnimalRecognitionDemo

This demo combines several [Redis](https://redis.io) data structures and [Redis Modules](https://redis.io/topics/modules-intro)
to process a stream of images and filter out the images that contain cats.

It uses:

* Redis Streams to capture the input video stream: `all`
* [RedisGears](https://oss.redislabs.com/redisgears/) to process this stream
* [RedisAI](https://oss.redislabs.com/redisai/) to classify the images with MobilenetV2

It forwards the images that contain cats to a stream: `cats`

## Architecture
![Architecture](/architecture.png)

## Requirements
Docker and Python 2

## Running the Demo
To run the demo:
```
$ git clone https://github.com/RedisGears/AnimalRecognitionDemo.git
$ cd AnimalRecognitionDemo
# If you don't have it already, install https://git-lfs.github.com/ (On OSX: brew install git-lfs)
$ git lfs install && git lfs fetch && git lfs checkout
$ docker-compose up
```
If something went wrong, e.g. you skipped installing git-lfs, you need to force docker-compose to rebuild the containers
```
$ docker-compose up --force-recreate --build
```
Open a second terminal for the video capturing:
```
$ pip install -r camera/requirements.txt
$ python camera/read_camera.py
```

## UI
* `http://localhost:3000` shows all the captured frames
* `http://localhost:3001` shows only the framse with cats

## Limitations
This demo is designed to be easy to setup, so it relies heavily on docker.
You can get better performance and a higher FPS by runninng this demo outside docker.
To control the FPS, edit the [gear.py](https://github.com/RedisGears/AnimalRecognitionDemo/blob/master/app/gear.py#L53) file.
