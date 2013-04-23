#!/usr/bin/env python
# coding: utf-8

import webim

u = {'id': '1', 'nick': 'nick', 'status': 'online', 'show': "hahaha"}

c = webim.Client(u, 'localhost', 'apikey', 'ticket', port=8000, timeout=40)

c.online(['2','3','4'], ['5'])

c.presence('online', 'hahaha')

c.message('1', 'hello...', '', '192838')

c.status('1', 'typing...')

c.members('group:1')

c.join('group:1')

c.leave('group:1')

import time
import urllib2

loops = 10

while(loops > 0):
  try:
    c.poll()
  except urllib2.HTTPError, e:
    print e
  loops -= 1
  time.sleep(5)

c.offline()
