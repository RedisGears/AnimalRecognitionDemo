# AnimalRecognitionDemo

## Rrequirements
Docker, Python 2 and pip

## Running the Demo
```
$ git clone https://github.com/RedisGears/AnimalRecognitionDemo.git
$ cd AnimalRecognitionDemo
# If you don't have it already, install https://git-lfs.github.com/
$ git lfs install; git lfs checkout
$ docker-compose up
```
Camera Capturing needs to happen in a second terminal
```
$ pip install camera/requirements.txt
$ python camera/read_camera.py
```

## UI

* On `http://localhost:3000` you will be able to see all the captured frames
* On `http://localhost:3001` you will see only cats
