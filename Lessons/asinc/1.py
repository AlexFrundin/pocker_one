import socket
import time
import sys

s=socket.socket()
s.connect(('localhost',5000))

while True:
    s.sendall(b'Hello' + sys.argv[1].decode('utf-8'))
    data=s.recv(1024)
    print(data)
    time.sleep(1)
