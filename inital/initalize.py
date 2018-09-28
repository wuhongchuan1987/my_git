#!/usr/bin/env python
#coding:utf-8

import os
import time
from pyinotify import ProcessEvent,WatchManager,Notifier,IN_CREATE,IN_MODIFY,IN_DELETE,WatchManagerError,PyinotifyError
import datetime
import hashlib
import subprocess
import ConfigParser

from mylib.alamod import get_netip

mask = IN_MODIFY | IN_DELETE
path = [ ]
m_file = [ ]

class Config(object):
	def __init__(self):
		self.formatime = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H:%M:%S')
		self.ip = get_netip.get_netip().get('netip')	
		self.config = ConfigParser.ConfigParser()
		self.curcfgpos = os.path.abspath(os.path.join(os.getcwd(), ".")) + '/config'
		#self.config.read(self.curcfgpos)
		self.topcfgpos = os.path.abspath(os.path.join(os.getcwd(), "..")) + '/config'
		if not os.path.exists(self.curcfgpos) and not os.path.exists(self.topcfgpos):
			pass
		elif not os.path.exists(self.curcfgpos):
			self.config.read(self.topcfgpos)
		else:
			self.config.read(self.curcfgpos)
	def get(self,*args):
		l = len(args)
        	try:
                	if l == 1:
                        	return self.config.items(args[0])
                	elif l == 2:
                        	return self.config.get(args[0],args[1])
        	except (ConfigParser.NoSectionError,ConfigParser.NoOptionError) ,e:
                	base.MQ.put("%s [ERROR] 配置文件读取错误：%s"%(base.TIME(),e))
	def get_sections(self):
		return self.config.sections()

conf = Config()

class FSMonitor(ProcessEvent):
        def process_default(self,event):
                if event.name.endswith('.swp') or event.name.endswith('.swpx') or event.name.endswith('~') or event.name.endswith('.swo'):
			pass
		elif event.maskname == 'IN_MODIFY':
			pass
		elif event.maskname == 'IN_DELETE':
			print '[WARNING] %s Deleted!'%(event.pathname)

        def process_IN_MODIFY(self,event):
                self.process_default(event)
	def process_IN_DELETE(self,event):
		self.process_default(event)

class CheckHash(object):
	def __init__(self,fs):
		self.hash = {}
		for f in fs:
			self.hash.setdefault(f,self.hash_file(f))
		self.iptables = self.hash_iptables()

	def hash_iptables(self):
		return	subprocess.Popen("iptables -nL|md5sum|awk '{print $1}'",stdout=subprocess.PIPE,shell=True).stdout.readline().strip()
	
	def hash_file(self,f):
		if os.path.exists(f):
			return hashlib.md5(open(f).read()).hexdigest()	
		else:
			print '[ERROR] 监控文件不存在:%s'%f
	def check(self):
		ret = [ ]
		tmp_hash = None
		for f in self.hash.keys():
			tmp_hash = self.hash_file(f)
			ret.append(tmp_hash)
		tmp_hash = self.hash_iptables()
		return (self.hash.keys(),ret)

wm = WatchManager()
wm.add_watch(m_file,mask)
notifier = Notifier(wm,FSMonitor())

notifier.process_events()
if notifier.check_events(600):
        notifier.read_events()
