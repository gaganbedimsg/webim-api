#!/usr/bin/env python
# coding: utf-8

"""
  www.webim20.cn
  ~~~~~~~
  API Test Server
  :copyright: (c) 2013 by Ery Lee(ery.lee at gmail.com)
"""

from flask import Flask, request, jsonify, url_for, render_template

APIVSN='v4'

app = Flask(__name__)

app.debug = True

@app.before_request
def before_reqest():
  if request.method == "POST":
    print request.form

@app.route("/")
def index():
  apis = [('POST', url_for(rule.endpoint)) 
            for rule in app.url_map.iter_rules() 
              if 'POST' in rule.methods]
  return render_template("/index.html", apis = apis)

@app.route("/v4/presences/online", methods=["POST"])
def online():
  nick = request.form['nick']
  name = request.form['name']
  domain = request.form['domain']
  version = request.form['version']
  groups = request.form['groups']
  buddies = request.form['buddies']
  show = request.form['show']
  status = request.form['status']
  #TODO:FIXME
  return jsonify({'ticket': 'ticketid',
                  'groups': [],
                  'buddies': []})

@app.route("/v4/presences/offline", methods=["POST"])
def offline():
  ticket = request.form['ticket']
  domain = request.form['domain']
  return "ok"
  
@app.route("/v4/presences/show", methods=["POST"])
def presence():
  ticket = request.form['ticket']
  domain = request.form['domain']
  nick = request.form['nick']
  show = request.form['show']
  status = request.form['status']
  return "ok"
  
@app.route("/v4/messages", methods=["POST"])
def messages():
  ticket = request.form['ticket']
  domain = request.form['domain']
  to = request.form['to']
  body = request.form['body']
  nick = request.form['nick']
  style = request.form['style']
  timestamp = request.form['timestamp']
  return "ok"

@app.route("/v4/statuses", methods=["POST"])
def statuses():
  ticket = request.form['ticket']
  domain = request.form['domain']
  nick = request.form['nick']
  show = request.form['show']
  return "ok"

@app.route("/v4/group/members", methods=["POST"])
def members():
  ticket = request.form['ticket']
  domain = request.form['domain']
  group = request.form['group']
  return jsonify({group: [{'id': '1', 'nick': 'nick'}]})

@app.route("/v4/group/leave", methods=["POST"])
def leave():
  ticket = request.form['ticket']
  domain = request.form['domain']
  group = request.form['group']
  nick = request.form['nick']
  return "ok"

@app.route("/v4/group/join", methods=["POST"])
def join():
  ticket = request.form['ticket']
  domain = request.form['domain']
  group = request.form['group']
  nick = request.form['nick']
  return jsonify({group: 1})

if __name__ == "__main__":
    app.run(host="0.0.0.0")

