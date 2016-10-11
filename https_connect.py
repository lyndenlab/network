#!/usr/bin/python


#import socket
import urllib2

#s = socket.socket()
#s.connect(("v157-7-211-189.myvps.jp",80))

response = urllib2.urlopen('http://157.7.211.189')
html = response.read()
print (html)
#s.close()
