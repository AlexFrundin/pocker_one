import socket

s=socket.socket()

s.connect(('localhost',5000))

s.sendall(b'Hello')

data=s.recv(1024)

print(data.encode('utf-8'))
s.close()
