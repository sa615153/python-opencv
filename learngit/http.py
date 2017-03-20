某ppt

制作get与post

import urllib2

def http_get():
	url='http://127.0.0.1:5000/dispatcher/AvailableTaskPCMatch'
	response = urllib2.urlopen(url)
	return response.read()

ret = http_get()
print("RET %r" % (ret))
----------------------------

import urllib
import urllib2
import json

def http_post():
	url = 'http://127.0.0.1:5000/PC/jobdone'
	values = {'user':"Smith",'passwd':'123456'}

	jdata = json.dump(values)
	req = urllib2.Request(url,jdata)
	response = urllib2.urlopen(req)
	return response.read()

resp = http_post()
print resp




