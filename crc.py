#!/usr/bin/python
import binascii
import time
start = time.clock()
string1 = 'abc'
attempt = 0
myhash = binascii.crc32(string1)
print "Trying now.."
while True:
	accstring = str(attempt)
	crchash = binascii.crc32(accstring)
	if crchash == myhash:
		print("Attempts: %i Collision: %s and %s" % (attempt, string1, accstring))
		break
	if attempt % 1000000 == 0:
		print 'Attempt %i: %s != %s' % (attempt, crchash, myhash)
		current_time = time.clock()
		elapsed = current_time - start
		print("speed: ", round(attempt/elapsed, 1), " iterations/second")
	attempt += 1

