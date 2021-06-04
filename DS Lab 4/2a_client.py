#Client Side
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9991
s.connect((host,port))
tm = s.recv(1024)
print("Time from Server:",tm.decode())
s.close()