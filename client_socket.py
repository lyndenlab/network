#!/usr/bin/python

import socket

s = socket.socket()
host = "v157-7-211-189.myvps.jp"
port = 30012

s.connect((host,port))
print s.recv(1024)
s.close
