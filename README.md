# AnimalRecognitionDemo

This demo combines several [Redis](https://redis.io) Data structures and [Redis Modules](https://redis.io/topics/modules-intro) to filter a stream of images that contain cats.  It utilises Redis Streams for capturing the input video stream:`all`.  [RedisGears](https://oss.redislabs.com/redisgears/) will process this stream and will call [RedisAI](https://oss.redislabs.com/redisai/) for image classification with MobilenetV2.  In case the stream contains cats, it will forward the images to a  stream:`cats`.

## Architecture
![Architecture](/architecture.png)


## Requirements
Docker and Python 2

## Running the Demo
```
$ git clone https://github.com/RedisGears/AnimalRecognitionDemo.git
$ cd AnimalRecognitionDemo
# If you don't have it already, install https://git-lfs.github.com/
$ git lfs install && git lfs fetch && git lfs checkout
$ docker-compose up
```
Open a second terminal for the video capturing.
```
$ pip install -r camera/requirements.txt
$ python camera/read_camera.py
```

## UI
* On `http://localhost:3000` you will be able to see all the captured frames
* On `http://localhost:3001` you will see only cats

## Limitations
This demo aimed at ease of setup and is hence heavily relying on docker.  Better performance and a higher FPS can be achieved by runninng this demo outside docker.  To control the FPS, look [here](https://github.com/RedisGears/AnimalRecognitionDemo/blob/master/app/gear.py#L53)
