#Server side
import socket
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

while(True):
	bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
	message = bytesAddressPair[0]
	address = bytesAddressPair[1]
	clientMsg = "Message from Client:{}".format(message)
	print(clientMsg)
	Input = input('Server Say Something: ')
	bytesToSend = str.encode(Input)
	UDPServerSocket.sendto(bytesToSend,address)