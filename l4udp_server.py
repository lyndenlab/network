#!/usr/local/bin/python

import socket

ipaddr = "0.0.0.0"
port = 30000
buff = 1024

def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server.bind((ipaddr, port))
	
	while True:
		print (server.recv(buff))

if __name__ == '__main__':
	main()
