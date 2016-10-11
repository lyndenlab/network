#!/usr/bin/python

import urllib2

request = urllib2.urlopen('http://157.7.211.189')
html = request.read()
print (html)
