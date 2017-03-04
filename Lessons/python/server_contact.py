import socket
from spravochnik_v2 import *

s=socket.socket()
s.bind(('localhost',5000))
s.listen(5)

c,a=s.accept()
print('connected:',a)
while True:
    data=c.recv(256)
    c.sendall(view_menu().encode('utf-8'))
    #c.sendall(data)
    data=c.recv(256)
    print(data)
c.close()
s.close()
