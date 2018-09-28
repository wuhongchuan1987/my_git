#!/usr/local/bin/python2.7
# coding=utf-8

import os
import sys
import time
import datetime
import json

from mylib.inital import initalize

class Send_WN_DD(object):
	def __init__(self):
		self.f =  os.path.abspath(os.path.join(os.getcwd(), "..")) + '/alamod/staffinfo.txt'
		self.bsdt = os.path.abspath(os.path.join(os.getcwd(), "..")) + '/alamod/bsdt_alarm.py'
		#self.f = '/usr/lib64/python2.7/site-packages/mylib/alamod/staffinfo.txt'
		#self.bsdt = '/usr/lib64/python2.7/site-packages/mylib/alamod/bsdt_alarm.py'
		self.res = initalize.conf.get('email','receivers')
		self.dd = initalize.conf.get('dtalk','ddid')

		with open(self.f, 'rb') as f1:
			self.t_info = f1.read()

	def getPhone(self):
		phls = [ ]
		for i in self.res.split(','):
			for j in json.loads(self.t_info):
				if j.get('en_name') == i:
					phls.append(j.get('phone'))
		return phls
	
	def send_dd(self,INFO):
		cmd = os.popen('python %s %s %s %s' % (self.bsdt,INFO,self.dd,self.getPhone())).read()

senwn = Send_WN_DD()
