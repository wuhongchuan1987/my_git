#!/usr/bin/env python
# coding=utf-8

import urllib2
import json,sys

import send_dd 

info = sys.argv[1]
ddid = sys.argv[2]
at = sys.argv[3]

url="""https://oapi.dingtalk.com/robot/send?access_token=%s""" %ddid
data = {
    "msgtype": "markdown",
    "markdown": {
        "title":"告警",
        "text": "%s" % (info.replace('#','\n\n>')),
    },
    "at": {
        "atMobiles": send_dd.senwn.getPhone(),
        "isAtAll": "false"
    }
}

headers = {'Content-Type': 'application/json'}
request = urllib2.Request(url=url, headers=headers, data=json.dumps(data))
response = urllib2.urlopen(request)
print response.read()
