#!/usr/local/bin/python

import socket
import threading

ipaddr = "0.0.0.0"
port = 30000

def handle_client(client_socket):
	request	= client_socket.recv(2048)	
	print ("[*] Recieved: %s", %request)
	client_socket.send("ACK!")
	client_socket.close()

def main():
	server = socket.socket(AF_INET, SOCK_STREAM)
	server.bind((ipaddr, port))
	server.listen(5)

	while True:
		client, addr = server.accept()
		client_handler = threading.Thread(target=handle_client, args=(client,))		
		client_handler.start()	

if __name__ == '__main__':
	main()
