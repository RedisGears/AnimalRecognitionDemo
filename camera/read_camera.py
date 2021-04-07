
import argparse
import cv2
import redis
import time
import sys
import os

try:
    import urllib.parse
except ImportError:
    import urllib.parse as urlparse

IMAGE_WIDTH = 640
IMAGE_HEIGHT = 480

MAX_IMAGES = 1000 # 5

class Webcam:
    def __init__(self, infile=0, fps=15.0):
        self.cam = cv2.VideoCapture(infile)
        self.cam.set(cv2.CAP_PROP_FPS, fps)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, IMAGE_WIDTH)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, IMAGE_HEIGHT)

    def __iter__(self):
        self.count = -1
        return self

    def __next__(self): # Python 2.7
        self.count += 1

        # Read image
        ret_val, img0 = self.cam.read()
        assert ret_val, 'Webcam Error'

        # Preprocess
        # img = cv2.flip(img0, 1)
        img = img0

        return self.count, img

    def __len__(self):
        return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='Input file (leave empty to use webcam)', nargs='?', type=str, default=None)
    parser.add_argument('-o', '--output', help='Output stream key name', type=str, default='camera:0')
    parser.add_argument('-u', '--url', help='Redis URL', type=str, default='redis://localhost:6379')
    parser.add_argument('--fmt', help='Frame storage format', type=str, default='.jpg')
    parser.add_argument('--fps', help='Frames per second (webcam)', type=float, default=15.0)
    parser.add_argument('--maxlen', help='Maximum length of output stream', type=int, default=1000)
    parser.add_argument('--test', help='transmit image instead of reading webcam', action="store_true")
    args = parser.parse_args()

    # Set up Redis connection
    url = urllib.parse.urlparse(args.url)
    conn = redis.Redis(host=url.hostname, port=url.port)
    if not conn.ping():
        raise Exception('Redis unavailable')
    print('Connected to Redis')
    sys.stdout.flush()

    if args.test is False:
        print('Operating in camera mode')
        sys.stdout.flush()
        if args.infile is None:
            loader = Webcam(infile=0, fps=args.fps)
        else:
            loader = Webcam(infile=int(args.infile), fps=args.fps)

        for (count, img) in loader:
            _, data = cv2.imencode(args.fmt, img)
            msg = {
                'count': count,
                'image': data.tobytes()
            }
            _id = conn.execute_command('xadd', args.output, 'MAXLEN', '~', str(MAX_IMAGES), '*', 'count', msg['count'], 'img', msg['image'])
            print('count: {} id: {}'.format(count, _id))
            sys.stdout.flush()
    else:
        image_file = os.environ['ANIMAL'] + '.jpg'
        print('Operating in test mode with image ' + image_file)
        sys.stdout.flush()
        img0 = cv2.imread(image_file)
        img = cv2.resize(img0, (IMAGE_WIDTH, IMAGE_HEIGHT))
        _, data = cv2.imencode(args.fmt, img)
        count = 1
        while True:
            msg = {
                'count': count,
                'image': data.tobytes()
            }
            _id = conn.execute_command('xadd', args.output, 'MAXLEN', '~', str(MAX_IMAGES), '*', 'count', msg['count'], 'img', msg['image'])
            # print('count: {} rc: {} id: {}'.format(count, rc, _id))
            # sys.stdout.flush()
            count += 1
            time.sleep(0.1)
