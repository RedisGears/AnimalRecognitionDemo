import argparse
import cv2
import redis
try:
    import urllib.parse
except ImportError:
    import urllib.parse as urlparse

class Webcam:
    def __init__(self, infile=0, fps=15.0):
        self.cam = cv2.VideoCapture(infile)
        self.cam.set(cv2.CAP_PROP_FPS, fps)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

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
    args = parser.parse_args()

    # Set up Redis connection
    url = urllib.parse.urlparse(args.url)
    conn = redis.Redis(host=url.hostname, port=url.port)
    if not conn.ping():
        raise Exception('Redis unavailable')

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
        _id = conn.execute_command('xadd', args.output, 'MAXLEN', '~', '1000', '*', 'count', msg['count'], 'img', msg['image'])
        print(('count: {} id: {}'.format(count, _id)))
