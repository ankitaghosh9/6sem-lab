#Server Side
import time
import socket

servsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9991
servsock.bind((host,port))
servsock.listen(5)

while True:
	clientsock,addr = servsock.accept()
	print("Connected to :",str(addr))
	currT = time.ctime(time.time()) + "\r\n"
	clientsock.send(currT.encode())

clientsock.close()