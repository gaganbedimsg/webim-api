#!/usr/bin/env python
# coding: utf-8

import webim

u = {'id': '1', 'nick': 'nick', 'status': 'online', 'show': "hahaha"}

c = webim.Client(u, 'localhost', 'apikey', 'ticket', port=5000)

c.online(['2','3','4'], ['5'])

c.presence('online', 'hahaha')

c.message('1', 'hello...', '', '192838')

c.status('1', 'typing...')

c.members('group:1')

c.join('group:1')

c.leave('group:1')

