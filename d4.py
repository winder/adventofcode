#!/usr/bin/python

import sys
import hashlib

string = sys.argv[1]
count = 0

md = hashlib.md5()
while True:
  m = md.copy()
  m.update(string + str(count))
  if m.hexdigest().startswith('000000'):
    print "Answer: " + str(count)
    break
  count += 1
