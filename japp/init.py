import argparse
import redis
from urllib.parse import urlparse

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
    if not conn.ping():
        raise Exception('Redis unavailable')

    # Check if this Redis instance had already been initialized
    initialized = conn.exists(initialized_key)
    if initialized:
        print('Discovered evidence of a previous initialization - skipping.')
        exit(0)

#    # Load the RedisAI model
#    print('Loading model - ', end='')
#    with open('models/mobilenet_v2_1.4_224_frozen.pb', 'rb') as f:
#        model = f.read()
#        res = conn.execute_command('AI.MODELSET', 'mobilenet:model', 'TF', 'CPU', 'INPUTS', 'input', 'OUTPUTS', 'MobilenetV2/Predictions/Reshape_1', model)
#        print(res)

    # Load the gear
    print('Loading gear - ', end='')
    with open('gear.jar', 'rb') as f:
        gear = f.read()
        res = conn.execute_command('RG.JEXECUTE com.redis.AnimalRecognitionDemo.Server', gear)
        print(res)

    # Lastly, set a key that indicates initialization has been performed
    print('Flag initialization as done - ', end='')
    print(conn.set(initialized_key, 'miauw'))
