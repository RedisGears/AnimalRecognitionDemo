#!/usr/bin/env python

import os
import sys

def to_int(x):
	try:
		return int(x)
	except:
		if x == '':
			return 10
		return -1

if len(sys.argv) > 1:
	fields = sys.argv[1].split(':')
else:
	fields = ['']
fields = map(lambda x: to_int(x), fields)
row = ""
i = 0
n = len(fields)
for line in sys.stdin:
	s = line.strip()
	m = len(s)
	c = fields[i]
	i = i + 1
	if c != -1:
		if m > c:
			m = c
		s = s[0:m] + ' ' * (c - m)
		if i < n:
			s = s + ' '
		row = row + s
	if i == n:
		print(row)
		row = ''
		i = 0
