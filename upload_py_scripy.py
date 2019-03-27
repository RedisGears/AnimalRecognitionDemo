import redis
import sys

r1 = redis.Redis('localhost', 6379)
f = open(sys.argv[1], 'rt')
script = f.read()
res1 = r1.execute_command('rg.pyexecute', script)
print res1
print ''

