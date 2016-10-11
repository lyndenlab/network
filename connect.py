import socket

port = 1234
ip = "192.168.11.31"

skt = socket.socket()

skt.connect((ip,port))
skt.send("hello lain...")
message = skt.recieved()
print (message)
skt.close()
