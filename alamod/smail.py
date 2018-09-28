#!/usr/bin/env python
#coding:utf-8

import time

import bsem_alarm 
from mylib.inital import initalize

class MAIL(object):
		res = initalize.conf.get('email','receivers')
		receivers = bsem_alarm.getAddress(res,'email')
		cc_receivers = []

		def send_wn_mail(self,sub,con):
			subject = '%s' % sub
			content = '%s' % con
			bsem_alarm.sendEmailText(self.receivers, self.cc_receivers, subject, content)

senwm = MAIL()
