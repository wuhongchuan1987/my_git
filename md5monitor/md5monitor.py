#!/usr/bin/env python
#coding:utf-8

import sys
import os
import time

from mylib.inital import initalize
import judgement

def main():
	path = os.path.abspath(os.curdir)
	try:
		pid = os.fork()
		if pid > 0:
			sys.exit(1)    
	except OSError,e:
		print >>sys.stderr, "fork #1 failed:%d (%s)"%(e.errno,e.strerror)
		sys.exit(1)
	os.chdir(path) 	
	os.setsid() 	
	os.umask(0) 	
	try:
		pid = os.fork()
		if pid > 0:
			judgement.judgement()
			sys.exit(0)
	except OSError,e:
		print >>sys.stderr, "fork #2 failed: %d (%s)"%(e.errno,e.strerror)
		sys.exit(1)

while True:
	interval = float(initalize.conf.get('interval','time'))
	time.sleep(interval)
	if __name__ == '__main__':
		main()
