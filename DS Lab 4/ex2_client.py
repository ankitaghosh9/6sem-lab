#Client side
import socket
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
	Input = input('Client Say Something: ')
	bytesToSend = str.encode(Input)
	UDPClientSocket.sendto(bytesToSend, serverAddressPort)
	msgFromServer = UDPClientSocket.recvfrom(bufferSize)
	msg = "Message from Server {}".format(msgFromServer[0])
	print(msg)