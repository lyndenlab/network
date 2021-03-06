#!/usr/local/bin/python

import socket
import threading

ipaddr = "0.0.0.0"
port = 30000
buff = 1024

def handle_client(client_socket):
	request	= client_socket.recv(buff)
	print ("Recieved:", request)
	client_socket.send("ACK!\n")
	client_socket.close()

def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((ipaddr, port))
	server.listen(5)

	while True:
		client, addr = server.accept()
		client_handler = threading.Thread(target=handle_client, args=(client,))
		client_handler.start()

if __name__ == '__main__':
	main()
