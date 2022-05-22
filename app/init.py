import argparse
import redis
from urllib.parse import urlparse

def waitForRDBLoad(conn):
    while True:
        try:
            if not conn.execute_command('info', 'Persistence')['loading']:
                break
        except redis.exceptions.BusyLoadingError:
            pass

if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='Redis URL', type=str, default='redis://127.0.0.1:6379')
    args = parser.parse_args()

    # Set up some vars
    initialized_key = 'cats:initialized'

    # Set up Redis connection
    url = urlparse(args.url)
    conn = redis.Redis(host=url.hostname, port=url.port)
    waitForRDBLoad(conn)
    if not conn.ping():
        raise Exception('Redis unavailable')

    # Check if this Redis instance had already been initialized
    initialized = conn.exists(initialized_key)
    if initialized:
        print('Discovered evidence of a previous initialization - skipping.')
        exit(0)

    # Load the RedisAI model
    print('Loading model - ', end='')
    with open('models/mobilenet_v2_1.4_224_frozen.pb', 'rb') as f:
        model = f.read()
        res = conn.execute_command('AI.MODELSTORE', 'mobilenet:model', 'TF', 'CPU', 'INPUTS', '1', 'input', 'OUTPUTS', '1', 'MobilenetV2/Predictions/Reshape_1', 'BLOB', model)
        print(res)

    # Load the gear
    print('Loading gear - ', end='')
    with open('gear.py', 'rb') as f:
        gear = f.read()
        res = conn.execute_command('RG.PYEXECUTE', gear, "REQUIREMENTS", 'imageio', 'opencv-python-headless<4.5')
        print(res)

    while True:
        res = conn.execute_command('RG.PYDUMPREQS')
        finished = True
        for i in range(len(res)):
            dep = res[i]
            downloaded_dep = dep[5]
            finished = finished and (downloaded_dep == b'yes')
        if finished:
            print('gear loaded')
            break

    # Lastly, set a key that indicates initialization has been performed
    print('Flag initialization as done - ', end='')
    print(conn.set(initialized_key, 'meow'))
