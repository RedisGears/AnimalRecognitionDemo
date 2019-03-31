import redis
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                 description='Test Framework for redis and redis module')

parser.add_argument(
    '--host', default='localhost',
    help='redis host')

parser.add_argument(
    '--port', default=6379, type=int,
    help='redis port')


parser.add_argument(
    '--file-path', default=None,
    help='script path')

args = parser.parse_args()

r = redis.Redis(args.host, args.port)
f = open(args.file_path, 'rt')
script = f.read()
res = r.execute_command('rg.pyexecute', script)
print res
print ''
