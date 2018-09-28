#!/usr/bin/env python
#coding:utf-8

import os
import time

from mylib.inital import initalize 
from mylib.alamod import send_dd
#from mylib.alamod import smail 

def judgement():
    filels = initalize.conf.get('monit','file')
    walkfile = filels.split(':')
    interval = float(initalize.conf.get('interval','time'))
    subnowt = initalize.conf.get('email','subnowt')
    subnerr = initalize.conf.get('email','subnerr') 

    ls1 = []
    for i in range(len(walkfile)):
        md5 = os.popen('md5sum %s' % (walkfile[i])).read().strip()
        ls1.append(md5)
    time.sleep(interval)

    ls2 = []
    for j in range(len(walkfile)):
        md5 = os.popen('md5sum %s' % (walkfile[j])).read().strip()
        ls2.append(md5)
                           
    for k in range(len(ls2)):
        if ls1[k] != ls2[k]:
             info = '%s#%s#%s#%s' % (subnerr,initalize.conf.formatime,initalize.conf.ip,walkfile[k]) 
             send_dd.senwn.send_dd('%s' % (info))

