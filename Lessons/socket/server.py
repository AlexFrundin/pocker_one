import socket

s=socket.socket()

s.bind(('localhost',5000))
s.listen(5)
print('Server started')

c,a=s.accept()
print('connected:',a)

data=c.recv(1024)
print(data)
c.sendall(data)
c.close()
s.close()
