import socket
import collector

sock = socket.socket()
sock.connect(('localhost', 9090))
inf=open('info.txt','rb').read()
sock.send(bytes(inf))
print(inf)

data = sock.recv(1024)
sock.close()

print(data)
