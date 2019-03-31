# AnimalRecognitionDemo

## Running the Demo

* run redis with RedisAI and RedisGears loaded.

* Uploaded the mobilenet_v2_1.4_224_frozen.pb model into a key called `m`:
```
redis-cli -x AI.MODELSET m TF CPU INPUTS input OUTPUTS MobilenetV2/Predictions/Reshape_1 < ./mobilenet_v2_1.4_224_frozen.pb
```

* Upload the `animal_name.py` script to redis using `upload_py_scripy.py`:
```
python upload_py_scripy.py --file-path ./animal_name.py
```

* Enter the `CameraCload/` directory and perform:
	* `npm install`
	* `PORT=3000 STREAM=all node server.js`
	* `PORT=3001 STREAM=cats node server.js`

* Start streaming frames to the redis:
```
python read_camera.py
```

* On `http://localhost:3000` you will be able to see all the captured frames
* On `http://localhost:3001` you will see only cats
