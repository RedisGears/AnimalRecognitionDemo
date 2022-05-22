[![license](https://img.shields.io/github/license/RedisGears/AnimalRecognitionDemo.svg)](https://github.com/RedisGears/AnimalRecognitionDemo)
[![Animal Recognition](https://github.com/RedisGears/AnimalRecognitionDemo/actions/workflows/ci-config.yml/badge.svg)](https://github.com/RedisGears/AnimalRecognitionDemo/actions/workflows/ci-config.yml)
[![Forum](https://img.shields.io/badge/Forum-RedisGears-blue)](https://forum.redislabs.com/c/modules/redisgears)
[![Discord](https://img.shields.io/discord/697882427875393627)](https://discord.gg/6yaVTtp)

# AnimalRecognitionDemo

This demo combines several [Redis](https://redis.io) data structures and [Redis Modules](https://redis.io/topics/modules-intro)
to process a AnimalRecognitionDemostream of images and filter out the images that contain cats.

It uses:

* Redis Streams to capture the input video stream: `all`
* [RedisGears](https://oss.redislabs.com/redisgears/) to process this stream
* [RedisAI](https://oss.redislabs.com/redisai/) to classify the images with MobilenetV2

It forwards the images that contain cats to a stream: `cats`

## Architecture
![Architecture](/architecture.png)

## Requirements
Docker and Python 3

## Running the Demo
To run the demo:
```bash
git clone https://github.com/RedisGears/AnimalRecognitionDemo.git
cd AnimalRecognitionDemo
# If you don't have it already, install https://git-lfs.github.com/ (On OSX: brew install git-lfs)
git lfs install && git lfs fetch && git lfs checkout
```
For running the demo with `make`, run:
```bash
make start
make camera
```
Then open the [UI](README.md#ui) to watch the result streams.

To end the demo, then to stop the containers:
```bash
make stop
```
Run `make help` for a few more options.

For running the demo manually, run:
```bash
docker-compose up
```
If something went wrong, e.g. you skipped installing git-lfs, you need to force docker-compose to rebuild the containers
```bash
docker-compose up --force-recreate --build
```
Open a second terminal for the video capturing:
```bash
pip install -r camera/requirements.txt
python camera/read_camera.py
```
Or run the camera process in test mode (without streaming from your camera):
```bash
ANIMAL=[cat|dog] python camera/read_camera.py --test
```

## UI
* `http://localhost:3000` shows all the captured frames
* `http://localhost:3001` shows only the framse with cats

## Limitations
This demo is designed to be easy to setup, so it relies heavily on docker.
You can get better performance and a higher FPS by runninng this demo outside docker.
To control the FPS, edit the [gear.py](https://github.com/RedisGears/AnimalRecognitionDemo/blob/master/app/gear.py#L53) file.
