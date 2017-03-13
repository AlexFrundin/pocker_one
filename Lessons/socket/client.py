import socket

s=socket.socket()

s.connect(('192.168.0.88',49845))

s.sendall(b'Hello')

data=s.recv(1024)

print(data.encode('utf-8'))
s.close()
