import argparse
import redis
from urllib.parse import urlparse

if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='Redis URL', type=str, default='redis://127.0.0.1:6379')
    parser.add_argument('--with-requirements', action="store_true", help="Present requirements to Gears")
    parser.add_argument('--no-requirements', action="store_true", help="Do not present requirements to Gears")
    args = parser.parse_args()

    # Set up some vars
    initialized_key = 'cats:initialized'

    # Set up Redis connection
    url = urlparse(args.url)
    conn = redis.Redis(host=url.hostname, port=url.port)
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
        res = conn.execute_command('AI.MODELSET', 'mobilenet:model', 'TF', 'CPU', 'INPUTS', 'input', 'OUTPUTS', 'MobilenetV2/Predictions/Reshape_1', 'BLOB', model)
        print(res)

    # Load the gear
    print('Loading gear - ', end='')
    with open('gear.py', 'rb') as f:
        gear = f.read()
        if not args.no_requirements:
            res = conn.execute_command('RG.PYEXECUTE', gear, 'REQUIREMENTS', 'imageio', 'numpy', 'opencv-python')
        else:
            res = conn.execute_command('RG.PYEXECUTE', gear)
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
    print(conn.set(initialized_key, 'miauw'))
