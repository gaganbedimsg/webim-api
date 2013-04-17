#!/usr/bin/env python
# coding: utf-8

"""
python webim client

Overview
========

See U{the WebIM homepage<http://www.github.com/webim>} for more about webim.

Usage summary
=============

This should give you a feel for how this module operates::

    import webim 
    c = webim.Client('domain', 'apikey', host='127.0.0.1', port = 8000)
    c.online('1,2,3', 'grp1, grp2, grp3')
    c.offline()

Detailed Documentation
======================

More detailed documentation is available in the L{Client} class.
"""

__author__    = "Ery Lee <ery.lee@gmail.com>"
__version__ = "4.0.0beta"
__copyright__ = "Copyright (C) 2013 Ery Lee"
__license__   = "Python Software Foundation License"

APIVSN = '4.0'

try:
  import json
except ImportError:
  import simplejson as json

import urllib2

class WebIMError(Exception):
    pass

class Client:
  
  def __init__(self, user, domain, apikey, ticket=None, host = 'localhost', port=8000):
    """
    Create a new Client object with the given host and port

    @param host: host
    @param port: port
    """
    self.user = user
    self.domain = domain 
    self.apikey = apikey
    self.ticket = ticket
    self.host = host
    self.port = port

  def online(self, buddies, groups):
    """
    Client online
    """
    reqdata = {
      'version' : APIVSN,
			'rooms': ','.join(groups), 
			'buddies': ','.join(buddies),
			'domain': self.domain, 
			'apikey': self.apikey, 
			'name': self.user['id'], 
			'nick': self.user['nick'], 
			'status': self.user['status'], 
			'show': self.user['show']
    }
    if self.user.is_visitor():
      reqdata['visitor'] = True
    
    status, body = _httpost(self, '/presences/online', reqdata)
    if(status != 200):
      return {'success': False, 'error_msg': body}
    respdata = json.loads(body)
    self.ticket = respdata['ticket']
    conninfo = {'ticket': self.ticket,
                'domain': self.domain,
                'server': "http://%s:%d/packets" % (self.host, self.port)}
    return {'success': True,
            'connection': conninfo,
            'buddies': respdata['buddies'],
            'rooms': respdata['rooms'],
            'server_time': 100101, #FIXME:
            'user': self.user}

  def offline(self):
    """
    Client offline
    """
    reqdata = {
      'version': APIVSN,
      'ticket' : self.ticket,
      'domain' : self.domain,
      'apikey' : self.apikey
    }
    status, body = _httpost(self, '/presences/offline', reqdata)
    return body

  def presence(self, show, status = ""):
    """
    Update Presence
    """
    reqdata = _newreq()
    reqdata['nick'] = self.user['nick']
    reqdata['show'] = show
    reqdata['status'] = status
    _status, body = _httpost(self, '/presences/show', reqdata)
    return body

  def message(self, to, body, style, timestamp, msgtype='unicast'):
    """
    Send Message
    """
    reqdata = _newreq()
    reqdata['nick'] = self.user['nick']
    reqdata['type'] = self.msgtype
    reqdata['to'] = to
    reqdata['body'] = body
    reqdata['style'] = style
    reqdata['timestamp'] = timestamp
    _status, body = _httpost(self, '/messages', reqdata)
    return body

  def status(self, to, show):
    """
    Send Status
    """
    reqdata = _newreq()
    reqdata['nick'] = self.user['nick']
    reqdata['to'] = to
    reqdata['show'] = show
    _status, body = _httpost(self, '/statuses', reqdata)
    return body

  def members(self, grpid):
    """
    Get group members
    """
    reqdata = _newreq()
    reqdata['room'] = grpid
    status, body = _httpost(self, '/room/members', reqdata)
    if status == 200:
      respdata = json.loads(body)
      return respdata[grpid]
    return None
     
  def join(self, grpid):
    """
    Join Group Chat
    """
    reqdata = _newreq()
    reqdata['nick'] = self.user['nick']
    reqdata['room'] = grpid
    status, body = _httpost(self, '/room/leave', reqdata)
    if status == 200:
      respdata = json.load(body)
      return {'id': grpid, 'count': respdata[grpid]}
    return None
  
  def leave(self, grpid):
    """
    Leave Group Chat
    """
    reqdata = _newreq()
    reqdata['nick'] = self.user['nick']
    reqdata['room'] = grpid
    _status, body = _httpost(self, '/room/leave', reqdata)
    return body
      

  def _newreq(self):
    return {
      'version': APIVSN,
      'domain': self.domain,
      'apikey': self.apikey,
      'ticket': self.ticket
    }
    
  def _httpost(self, path, data):
    url = "http://%s:%d/%s" % (self.host, self.port, path)
    try:
      resp = urllib2.urlopen(url, data)
      body = resp.read()
      return (resp.getcode(), body)
    except urllib2.HTTPError, e:
      raise e
 
